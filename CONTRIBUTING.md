# Contributing

The goal is to make quantum mechanics understandable and calculations reproducible.
Small corrections are welcome. Read the [current scope](README.md) and
[roadmap](ROADMAP.md) before beginning a large new chapter.

## Propose a change

1. Look for an existing issue describing the problem. If none exists, open one
   with the relevant file, equation or paper ID and a concrete explanation.
2. For larger changes, explain the intended learning outcome and prerequisites
   before writing a full chapter. For a typo or a clear bug, a focused PR is enough.
3. Create a branch or fork, make the change, and open a pull request describing
   the problem, the result and the checks you ran.

Do not include private data, passwords, access tokens or unpublished third-party
material. Security reports follow [SECURITY.md](SECURITY.md).

## Physics and teaching standards

- State the system, assumptions, units, basis and boundary conditions before a derivation.
- Show intermediate steps; distinguish a mathematical identity from a physical postulate.
- Verify dimensions, normalization, limiting cases and signs where relevant.
- Cite original papers or authoritative lecture material and use your own explanations.
- Supply worked answers for new exercises, including the method and assumptions.
- Label planned, incomplete and unreviewed material accurately. Passing code tests
  do not establish independent scientific review.

For the atlas, keep paper IDs stable and unique. Do not reuse an existing ID for
a different paper. The data format separates fields with `|`; equations may also
contain `|`, which the parser preserves between the summary and final URL/flag fields.
Use HTTPS source links and review the source before changing its bibliographic claim.

## Numerical changes

Explain the approximation and its failure modes. Use a known analytic result,
conservation law or independently converged reference as a check. A good test
should detect an incorrect physical result, not merely duplicate the implementation.
For grid methods, state grid spacing, boundary conditions, normalization convention,
and the difference between discretization error and domain truncation.

From the repository root, install the dependency and run the relevant checks:

```bash
python -m pip install -r requirements.txt
python -m unittest discover -s tests -p 'test_*.py' -v
node --test tests/atlas.test.js
python scripts/check_site.py
python scripts/build_site.py
```

Use Python 3.11+ (reference: 3.12) and Node.js 22 for these commands. Pure prose
corrections do not require new tests. For UI changes, inspect desktop and mobile
layouts and keyboard navigation. Report any check you could not run.

## Review and licensing

Keep a pull request focused. The maintainer checks correctness, sources, clarity,
scope and reproducibility. Review may request changes; no response deadline is promised.
Follow the [code of conduct](CODE_OF_CONDUCT.md).

Submit only material you have the right to contribute. Contributions to this
repository are made under its [MIT license](LICENSE). Link to copyrighted papers
instead of copying full texts. Credit genuine collaborators and sources.

AI tools can assist drafting or coding, but the contributor remains responsible
for every claim, derivation, citation and test. State material AI assistance in
the PR when it affects how the work should be reviewed. Never claim AI output was
independently verified unless that verification actually happened.
