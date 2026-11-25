# Contributing solved quantum problems

Thank you for improving this open-access educational project. The problem book currently contains 25 introductory problems. Please contribute original prose, derivations, corrections, references, and reproducible tests rather than copied chapters or copyrighted question banks.

## Propose a problem or correction

1. Open a GitHub issue with the **problem number**, an exact error or proposed topic, and a brief physical motivation.
2. Include the **assumptions, notation, coordinate system, units, and boundary conditions**.
3. Show the **question**, a worked **solution with intermediate steps**, and **physical intuition** explaining what the answer means.
4. Verify dimensionless probabilities, normalization, limiting cases, eigenvalues and signs where applicable. For numerical problems, include commands and a comparison with an analytic result, conservation law, or documented convergence study.
5. Cite sources actually consulted using stable URLs or bibliographic details; no made-up citations, arXiv IDs, peer review, downloads or project adoption claims.
6. Open a focused pull request. Disclose material AI assistance honestly and take responsibility for every published assertion. Reference any issue it resolves.

## Suggested problem format

```markdown
### N. A short title
**Prerequisites:** ...
**Assumptions and units:** ...
**Problem:** ...
**Step-by-step solution:** ...
**Physical intuition:** ...
**Verification and limitation:** ...
**References:** ...
```

The source is published under the repository's existing MIT license insofar as it consists of original materials contributed under that license. Do not assume that linked external textbooks, figures or papers are relicensed. For security or conduct issues use the repository's established policies when merged. Contributions and outside review are invited but are not represented as having already occurred.

## Building a public PDF

The workflow `.github/workflows/problem-book-pdf.yml` can convert `docs/QUANTUM_PROBLEM_BOOK.md` into a downloadable **GitHub Actions artifact** using Pandoc and LaTeX. It is a *build artifact*, not an arXiv submission. It is not automatically committed to the repository. Locally, with Pandoc and a TeX distribution installed:

```bash
pandoc docs/QUANTUM_PROBLEM_BOOK.md --standalone --pdf-engine=pdflatex \
  -V geometry:margin=24mm -V fontsize=11pt \
  -o quantum-problem-book.pdf
```

The downloadable PDF shared in the accompanying ChatGPT response is a more expanded, independently typeset edition with full derivations; the repository Markdown acts as the openly editable problem index.
