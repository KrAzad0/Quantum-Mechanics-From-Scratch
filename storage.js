/* Browser preferences only. Never put credentials or private data in this store. */
(function (root) {
  "use strict";
  const KEYS = Object.freeze({
    read: "qm-from-scratch:v1:read",
    theme: "qm-from-scratch:v1:theme"
  });

  function createStore(storageProvider, validIds) {
    const allowed = new Set(validIds);
    let available = true;
    function storage() {
      const value = storageProvider();
      if (!value) throw new Error("Browser storage is unavailable");
      return value;
    }
    function get(key) {
      try { return storage().getItem(key); }
      catch (_) { available = false; return null; }
    }
    function set(key, value) {
      try { storage().setItem(key, value); return true; }
      catch (_) { available = false; return false; }
    }
    function cleanIds(values) {
      if (!Array.isArray(values)) return [];
      return [...new Set(values.filter(id => Number.isInteger(id) && allowed.has(id)))];
    }
    return {
      readProgress() {
        try { return new Set(cleanIds(JSON.parse(get(KEYS.read) || "[]"))); }
        catch (_) { return new Set(); }
      },
      saveProgress(ids) { return set(KEYS.read, JSON.stringify(cleanIds([...ids]))); },
      readTheme() {
        const value = get(KEYS.theme) || get("qm-theme");
        return value === "light" ? "light" : "dark";
      },
      saveTheme(theme) { return set(KEYS.theme, theme === "light" ? "light" : "dark"); },
      // The old parser produced ambiguous IDs. Leave that data untouched; do not migrate it.
      hasLegacyProgress() { return get(KEYS.read) === null && get("qm-read") !== null; },
      isAvailable() { return available; }
    };
  }

  const api = { KEYS, createStore };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.QM_STORAGE = api;
})(typeof window === "undefined" ? globalThis : window);
