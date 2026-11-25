"use strict";
const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const { KEYS, createStore } = require("../storage.js");

const context = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(__dirname, "../papers.js"), "utf8"), context);
const papers = JSON.parse(JSON.stringify(context.window.QM_PAPERS));
const ids = papers.map(paper => paper.id);
function memory(values = {}) {
  const map = new Map(Object.entries(values));
  return { getItem: key => map.get(key) ?? null, setItem: (key, value) => map.set(key, value) };
}

test("the 41 papers retain every complete ID exactly once", () => {
  assert.deepEqual(ids, Array.from({ length: 41 }, (_, index) => index + 1));
  assert.equal(papers.find(paper => paper.id === 1).authors, "Max Planck");
  assert.equal(papers.find(paper => paper.id === 41).authors, "John S. Bell");
});

test("equations containing pipes do not corrupt links or the essential flag", () => {
  assert.match(papers.find(p => p.id === 40).equation, /TrB\|Ψ⟩⟨Ψ\|/);
  assert.match(papers.find(p => p.id === 41).equation, /\|S\|/);
  assert.equal(papers.filter(p => p.essential).length, 20);
  for (const paper of papers) {
    assert.equal(new URL(paper.link).protocol, "https:");
    assert.ok(paper.year >= 1900 && paper.year <= 1964);
    for (const field of ["title", "authors", "era", "summary", "equation"]) assert.ok(paper[field]);
  }
});

test("valid progress round-trips without duplicate or unknown IDs", () => {
  const backend = memory({ [KEYS.read]: '[1,1,11,41,0,42,"2",null,2.5]' });
  const store = createStore(() => backend, ids);
  assert.deepEqual([...store.readProgress()], [1, 11, 41]);
  store.saveProgress(new Set([2, 20, 41]));
  assert.deepEqual([...store.readProgress()], [2, 20, 41]);
});

test("malformed or unexpected stored JSON cannot prevent startup", () => {
  for (const input of ["not JSON", "null", "{}", '"hello"', "42"]) {
    const store = createStore(() => memory({ [KEYS.read]: input }), ids);
    assert.deepEqual([...store.readProgress()], []);
  }
});

test("a denied storage getter falls back without throwing", () => {
  const store = createStore(() => { throw new Error("SecurityError"); }, ids);
  assert.deepEqual([...store.readProgress()], []);
  assert.equal(store.readTheme(), "dark");
  assert.equal(store.saveProgress(new Set([1])), false);
  assert.equal(store.saveTheme("light"), false);
  assert.equal(store.isAvailable(), false);
});

test("a failed write leaves the current in-memory selection usable", () => {
  const backend = memory();
  backend.setItem = () => { throw new Error("QuotaExceededError"); };
  const store = createStore(() => backend, ids);
  const current = new Set([1, 41]);
  assert.equal(store.saveProgress(current), false);
  assert.deepEqual([...current], [1, 41]);
  assert.equal(store.isAvailable(), false);
});

test("ambiguous legacy progress is not migrated or erased", () => {
  const backend = memory({ "qm-read": "[0,1,2]", "qm-theme": "light" });
  const store = createStore(() => backend, ids);
  assert.equal(store.hasLegacyProgress(), true);
  assert.deepEqual([...store.readProgress()], []);
  assert.equal(store.readTheme(), "light");
  store.saveProgress(new Set([41]));
  assert.equal(store.hasLegacyProgress(), false);
  assert.equal(backend.getItem("qm-read"), "[0,1,2]");
});

test("theme values are restricted to light and dark", () => {
  const backend = memory({ [KEYS.theme]: "unexpected" });
  const store = createStore(() => backend, ids);
  assert.equal(store.readTheme(), "dark");
  store.saveTheme("light");
  assert.equal(store.readTheme(), "light");
  store.saveTheme("unexpected");
  assert.equal(backend.getItem(KEYS.theme), "dark");
});
