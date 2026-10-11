#!/usr/bin/env python3
import argparse
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RETIRED_NAMES = ("Concord", "RelayRPC")


def contrast_ratio(first: str, second: str) -> float:
    def luminance(value: str) -> float:
        channels = [int(value[index:index + 2], 16) / 255 for index in (1, 3, 5)]
        linear = [channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4
                  for channel in channels]
        return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]
    high, low = sorted((luminance(first), luminance(second)), reverse=True)
    return (high + 0.05) / (low + 0.05)


def links(markdown: str) -> list[str]:
    markdown_links = re.findall(r"!?\[[^]]*\]\(([^)\s]+)(?:\s+['\"][^)]*['\"])?\)", markdown)
    html_links = re.findall(r"(?:src|srcset|href)=['\"]([^'\"]+)['\"]", markdown)
    return markdown_links + html_links


def check_online(url: str) -> str | None:
    request = urllib.request.Request(url, headers={"User-Agent": "David-Lee-11101-profile-validator"})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            if response.status >= 400:
                return f"external link returned {response.status}: {url}"
    except (urllib.error.URLError, TimeoutError) as error:
        return f"external link failed: {url} ({error})"
    return None


def validate(root: Path = ROOT, online: bool = False) -> list[str]:
    errors: list[str] = []
    readme = (root / "README.md").read_text(encoding="utf-8")
    for retired in RETIRED_NAMES:
        if retired.lower() in readme.lower():
            errors.append(f"retired portfolio name present: {retired}")
    for target in links(readme):
        if target.startswith("https://"):
            if online:
                failure = check_online(target)
                if failure:
                    errors.append(failure)
            continue
        if target.startswith(("http://", "mailto:")):
            errors.append(f"profile link must use HTTPS: {target}")
            continue
        local = (root / target.split("#", 1)[0]).resolve()
        if not local.exists():
            errors.append(f"local profile link does not exist: {target}")

    for svg_path in sorted((root / "assets").glob("*.svg")):
        svg = ET.parse(svg_path).getroot()
        if svg.get("role") != "img" or "title" not in (svg.get("aria-labelledby") or ""):
            errors.append(f"SVG accessibility metadata missing: {svg_path.name}")
        if not svg.get("viewBox"):
            errors.append(f"SVG viewBox missing: {svg_path.name}")
        background, foreground = svg.get("data-background"), svg.get("data-foreground")
        if not background or not foreground or contrast_ratio(background, foreground) < 7:
            errors.append(f"SVG primary contrast is below 7:1: {svg_path.name}")
    if len(list((root / "assets").glob("hero-*.svg"))) != 2:
        errors.append("expected one light and one dark hero SVG")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--online", action="store_true", help="also request external HTTPS links")
    args = parser.parse_args()
    failures = validate(online=args.online)
    if failures:
        print("\n".join(f"ERROR: {failure}" for failure in failures), file=sys.stderr)
        return 1
    print("profile validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
