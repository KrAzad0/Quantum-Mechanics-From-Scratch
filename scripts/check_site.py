"""Check local HTML references and repository learning links without network calls."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "https://github.com/KrAzad0/Quantum-Mechanics-From-Scratch/"


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        for attr in ("src", "href"):
            if attr in attrs:
                self.links.append(attrs[attr])


def main():
    parser = Links()
    parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))
    errors = []
    if len(parser.ids) != len(set(parser.ids)):
        errors.append("Duplicate HTML IDs")
    for link in parser.links:
        parsed = urlsplit(link)
        if parsed.scheme and parsed.scheme != "https":
            errors.append(f"Unexpected link protocol: {link}")
        elif link.startswith("#") and parsed.fragment not in parser.ids:
            errors.append(f"Missing anchor: {link}")
        elif not parsed.scheme and parsed.path and not (ROOT / unquote(parsed.path)).exists():
            errors.append(f"Missing asset: {link}")
        elif link.startswith(REPOSITORY):
            suffix = link[len(REPOSITORY):]
            if suffix.startswith(("blob/main/", "tree/main/")):
                target = suffix.split("/", 2)[2]
                if not (ROOT / target).exists():
                    errors.append(f"Missing learning file: {target}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"Checked {len(parser.links)} page links and assets; all local targets exist.")


if __name__ == "__main__":
    main()
