#!/usr/bin/env python3
"""Generate the animated stack panel, once per theme.

Replaces a markdown table. A table renders the same in every reader and says
"CV"; this says the same words but arrives, which is the whole difference the
profile was missing.

Restraint is the design here. Each pill fades and lifts once on load, staggered
left to right, and then everything stops. Nothing loops. A stack panel that
pulses forever competes with the header, which is the one thing on the page that
should be moving - and two things moving at once is how a profile starts looking
like a template rather than a page someone made.

Pill widths are computed from a per-character advance rather than measured, so
the label text and the box around it are laid out from one number. Getting that
wrong shows immediately as text spilling out of its pill, which is why the
advance is calibrated against the font size rather than guessed once and left.

Run:  python3 tools/make-stack.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from theme import MONO, SANS, THEMES, esc  # noqa: E402

ROWS = [
    ("Languages", ["TypeScript", "Python", "Rust", "Solidity"]),
    ("Agent rails", ["x402 v2", "MPP", "ERC-8004", "MCP", "LangChain", "CrewAI"]),
    ("Onchain", ["Base", "Solana", "viem", "Foundry", "Anchor"]),
    ("Backend", ["Node.js", "FastAPI", "PostgreSQL", "ChromaDB"]),
    ("Interfaces", ["React", "Vite", "vanilla HTML/CSS", "embeddable widgets"]),
    ("Supply chain", ["cosign", "SBOM", "provenance", "GHCR", "Docker"]),
]

W = 726
PAD_X = 34
LABEL_W = 132           # left gutter holding the row label
ROW_H = 46
TOP = 30
FONT = 13.5
CHAR_W = 7.45           # advance for FONT in the mono stack, measured not guessed
PILL_PAD = 13
GAP = 9
H = TOP + len(ROWS) * ROW_H + 18


def pill(x: float, y: float, label: str, t: dict, delay: float) -> tuple[str, float]:
    """One tag. Returns its markup and the x where the next one starts."""
    w = len(label) * CHAR_W + PILL_PAD * 2
    body = (
        f'<g opacity="0" transform="translate(0,6)">'
        f'<animate attributeName="opacity" from="0" to="1" dur="0.42s" '
        f'begin="{delay:.2f}s" fill="freeze"/>'
        f'<animateTransform attributeName="transform" type="translate" '
        f'from="0 6" to="0 0" dur="0.42s" begin="{delay:.2f}s" fill="freeze"/>'
        f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="27" rx="13.5" '
        f'fill="{t["pill"]}" stroke="{t["pillEdge"]}" stroke-width="1"/>'
        f'<text x="{x + w / 2:.1f}" y="{y + 18}" text-anchor="middle" '
        f'font-family="{MONO}" font-size="{FONT}" fill="{t["pillText"]}">{esc(label)}</text>'
        f'</g>'
    )
    return body, x + w + GAP


def build(theme: str) -> str:
    t = THEMES[theme]
    parts: list[str] = []
    step = 0.05

    for r, (label, tags) in enumerate(ROWS):
        y = TOP + r * ROW_H
        # Row label, with an accent tick that draws itself before its pills land.
        parts.append(
            f'<rect x="{PAD_X}" y="{y + 6}" width="3" height="16" rx="1.5" '
            f'fill="{t["accent0"]}" opacity="0">'
            f'<animate attributeName="opacity" from="0" to="0.9" dur="0.3s" '
            f'begin="{r * 6 * step:.2f}s" fill="freeze"/></rect>'
            f'<text x="{PAD_X + 14}" y="{y + 19}" font-family="{SANS}" font-size="13" '
            f'font-weight="600" fill="{t["muted"]}" opacity="0">{esc(label)}'
            f'<animate attributeName="opacity" from="0" to="1" dur="0.3s" '
            f'begin="{r * 6 * step:.2f}s" fill="freeze"/></text>'
        )

        x = float(PAD_X + LABEL_W)
        for i, tag in enumerate(tags):
            markup, x = pill(x, y, tag, t, r * 6 * step + 0.12 + i * step)
            parts.append(markup)

        if x > W - PAD_X:  # caught at build time rather than in the browser
            raise SystemExit(
                f"row '{label}' overflows: ends at {x:.0f}px, panel is {W}px"
            )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"
     viewBox="0 0 {W} {H}" role="img"
     aria-label="{esc('; '.join(f'{k}: {", ".join(v)}' for k, v in ROWS))}">
  <title>Stack</title>
  <defs>
    <linearGradient id="sbg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{t['bg0']}"/>
      <stop offset="100%" stop-color="{t['bg2']}"/>
    </linearGradient>
    <clipPath id="scard"><rect width="{W}" height="{H}" rx="16"/></clipPath>
  </defs>
  <g clip-path="url(#scard)">
    <rect width="{W}" height="{H}" fill="url(#sbg)"/>
    <rect width="{W}" height="{H}" fill="none" stroke="{t['pillEdge']}" stroke-width="1" rx="16"/>
    {"".join(parts)}
  </g>
</svg>
"""


def main() -> None:
    out = Path(__file__).resolve().parent.parent / "assets"
    out.mkdir(exist_ok=True)
    for theme in THEMES:
        path = out / f"stack-{theme}.svg"
        path.write_text(build(theme), encoding="utf-8")
        print(f"  wrote assets/{path.name} ({path.stat().st_size / 1024:.1f} kB)")
    print(f"  {sum(len(v) for _, v in ROWS)} tags over {len(ROWS)} rows, {H}px tall")


if __name__ == "__main__":
    main()
