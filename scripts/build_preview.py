"""Build the README layout study with local or embedded banner images."""

import argparse
import base64
from pathlib import Path
import re
import struct


ROOT = Path(__file__).resolve().parent.parent


def render(embed=False):
    page = (ROOT / "docs/index.template.html").read_text(encoding="utf-8")
    names = set(re.findall(r"\{\{image:([^}]+)\}\}", page))
    for name in names:
        source = ROOT / "docs/assets" / name
        if not source.is_file() or source.suffix != ".png":
            raise ValueError(f"Missing PNG asset: {name}")
        image = source.read_bytes()
        if image[:8] != b"\x89PNG\r\n\x1a\n":
            raise ValueError(f"Not a PNG asset: {name}")
        width, height = struct.unpack(">II", image[16:24])
        if width != 5 * height:
            raise ValueError(f"Banner must be exactly 5:1: {name} is {width} x {height}")
        value = "assets/" + name
        if embed:
            value = "data:image/png;base64," + base64.b64encode(image).decode("ascii")
        page = page.replace("{{image:" + name + "}}", value)
        page = page.replace("{{width:" + name + "}}", str(width))
        page = page.replace("{{height:" + name + "}}", str(height))
    if "{{" in page:
        raise ValueError("Unresolved template value")
    return page


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--embed", action="store_true", help="Create one portable HTML file")
    parser.add_argument("--output", type=Path, default=ROOT / "docs/index.html")
    parser.add_argument("--check", action="store_true", help="Check that the output matches the source")
    args = parser.parse_args()
    page = render(args.embed)
    if args.check:
        if not args.output.exists() or args.output.read_text(encoding="utf-8") != page:
            raise SystemExit(f"Preview needs rebuilding: {args.output}")
        print("Preview matches the template and assets.")
        return
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(page, encoding="utf-8")
    print(f"Built {args.output}")


if __name__ == "__main__":
    main()
