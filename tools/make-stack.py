#!/usr/bin/env python3
"""Generate the stack panel, once per theme.

Set as ledger lines, not tags. The first version put every technology in a
rounded pill on a rounded card with an accent rail down the side, which is three
of the tells that make a page read as machine-made, and it turned a list of
tools into a wall of lozenges nobody scans.

A ledger line is better suited to what this actually is: a label, then values,
on a ruled row. It reads left to right in one pass, the labels align, and
nothing decorates.

Motion settles the rows in once and then stops. The header already owns the one
element on the page that keeps moving.

Run:  python3 tools/make-stack.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from theme import MONO, MONO_ADV, THEMES, esc  # noqa: E402

ROWS = [
    ("LANGUAGES", ["TypeScript", "Python", "Rust", "Solidity"]),
    ("AGENT RAILS", ["x402 v2", "MPP", "ERC-8004", "MCP", "LangChain", "CrewAI"]),
    ("ONCHAIN", ["Base", "Solana", "viem", "Foundry", "Anchor"]),
    ("BACKEND", ["Node.js", "FastAPI", "PostgreSQL", "ChromaDB"]),
    ("INTERFACES", ["React", "Vite", "hand-written HTML/CSS", "embeddable widgets"]),
    ("SUPPLY CHAIN", ["cosign", "SBOM", "provenance", "GHCR", "Docker"]),
]

W = 1000
PAD = 52
LABEL_W = 190           # left column holding the label
ROW_H = 44
TOP = 34
VALUE_SIZE = 14
SEP = "  ·  "
H = TOP + len(ROWS) * ROW_H + 16


def build(theme: str) -> str:
    t = THEMES[theme]
    parts: list[str] = []
    overflow: list[str] = []

    for r, (label, values) in enumerate(ROWS):
        y = TOP + r * ROW_H
        line = SEP.join(values)
        delay = 0.15 + r * 0.07

        # Hairline above every row but the first: rules separate, they do not
        # frame, so the top edge stays open.
        if r:
            parts.append(
                f'<rect x="{PAD}" y="{y - 15}" width="{W - PAD * 2}" height="1" '
                f'fill="{t["ruleSoft"]}">'
                f'<animate attributeName="opacity" from="0" to="1" dur="0.5s" '
                f'begin="{delay:.2f}s" fill="freeze"/></rect>'
            )

        parts.append(
            f'<g opacity="1">'
            f'<animate attributeName="opacity" from="0" to="1" dur="0.5s" '
            f'begin="{delay:.2f}s" fill="freeze"/>'
            f'<text x="{PAD}" y="{y + 8}" font-family="{MONO}" font-size="10.5" '
            f'letter-spacing="2.6" fill="{t["faint"]}">{esc(label)}</text>'
            f'<text x="{PAD + LABEL_W}" y="{y + 8}" font-family="{MONO}" '
            f'font-size="{VALUE_SIZE}" fill="{t["text"]}">{esc(line)}</text>'
            f'</g>'
        )

        end = PAD + LABEL_W + len(line) * VALUE_SIZE * MONO_ADV
        if end > W - PAD:
            overflow.append(f"{label}: ends at {end:.0f}px of {W - PAD}")

    if overflow:                      # caught here, not in someone's browser
        raise SystemExit("row overflows: " + "; ".join(overflow))

    aria = ". ".join(f"{k}: {', '.join(v)}" for k, v in ROWS)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"
     viewBox="0 0 {W} {H}" role="img" aria-label="{esc(aria)}">
  <title>Stack</title>
  <rect width="{W}" height="{H}" fill="{t['ground']}"/>
  <rect x="0" y="0" width="4" height="{H}" fill="{t['brass']}">
    <animate attributeName="opacity" values="0;1" dur="0.6s" fill="freeze"/>
  </rect>
  {"".join(parts)}
</svg>
"""


def main() -> None:
    out = Path(__file__).resolve().parent.parent / "assets"
    out.mkdir(exist_ok=True)
    for theme in THEMES:
        path = out / f"stack-{theme}.svg"
        path.write_text(build(theme), encoding="utf-8")
        print(f"  wrote assets/{path.name} ({path.stat().st_size / 1024:.1f} kB)")
    print(f"  {sum(len(v) for _, v in ROWS)} values over {len(ROWS)} rows, {H}px tall")


if __name__ == "__main__":
    main()
