"""Stage only the public static-site assets; keep source and maintainer docs out."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_site"
FILES = ("index.html", "styles.css", "papers.js", "storage.js", "app.js", ".nojekyll")


def main():
    if OUTPUT.is_symlink():
        raise RuntimeError("Refusing to replace a symlink at _site")
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir()
    for filename in FILES:
        shutil.copy2(ROOT / filename, OUTPUT / filename)
    shutil.copytree(ROOT / "assets", OUTPUT / "assets")
    print("Static site staged in _site (HTML, CSS, JavaScript and assets only).")


if __name__ == "__main__":
    main()
