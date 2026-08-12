#!/usr/bin/env python3
"""Generate the profile header, once per theme.

Laid out as a record rather than a banner: the name as the party, a rule, then
labelled fields underneath. Left-aligned, square-cornered, one brass line.

The motion is deliberately small. Everything settles in once on load, and the
only thing that keeps moving afterwards is the FOCUS value, which cycles through
three positions the way a field updates rather than the way a terminal types.
A profile with several things looping is how a page starts feeling automated -
one moving element reads as considered, four read as a template.

Run:  python3 tools/make-header.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from theme import MONO, MONO_ADV, SANS, THEMES, esc  # noqa: E402

NAME = "Nolwen Sean Hononta"
REF = "github.com/4n0nn43x"

# The FOCUS field cycles. Three values, each held long enough to read twice.
FOCUS = [
    "fullstack - interface, API, chain",
    "agent payment rails - x402 v2, MPP",
    "onchain settlement - ERC-8004 verdicts",
]
HOLD = 3.6
FADE = 0.45
SLOT = HOLD + FADE
CYCLE = SLOT * len(FOCUS)

W, H = 1000, 218
PAD = 52
BASE_NAME = 96          # baseline of the name
RULE_Y = 124
FIELD_Y = 158           # baseline of the field labels
VALUE_Y = 186           # baseline of the field values


def field(x: int, label: str, value: str, t: dict, delay: float, mono: bool = True) -> str:
    """A labelled field: small tracked-out label, value beneath it."""
    face = MONO if mono else SANS
    return (
        f'<g opacity="1">'
        f'<animate attributeName="opacity" from="0" to="1" dur="0.5s" '
        f'begin="{delay:.2f}s" fill="freeze"/>'
        f'<text x="{x}" y="{FIELD_Y}" font-family="{MONO}" font-size="10.5" '
        f'letter-spacing="2.6" fill="{t["faint"]}">{esc(label)}</text>'
        f'<text x="{x}" y="{VALUE_Y}" font-family="{face}" font-size="14.5" '
        f'fill="{t["muted"]}">{esc(value)}</text>'
        f'</g>'
    )


def focus_field(x: int, t: dict) -> str:
    """The one element that keeps moving: a field whose value is replaced.

    Each value owns a slot in one indefinitely-repeating cycle rather than
    being scheduled with `begin` offsets. Offsets fire once: an earlier draft of
    this file used them and the line went permanently blank after twelve
    seconds, which only surfaced in a screenshot of the live profile.
    """
    parts = [
        f'<text x="{x}" y="{FIELD_Y}" font-family="{MONO}" font-size="10.5" '
        f'letter-spacing="2.6" fill="{t["faint"]}">FOCUS'
        f'<animate attributeName="opacity" from="0" to="1" dur="0.5s" '
        f'begin="0.55s" fill="freeze"/></text>'
    ]
    for i, value in enumerate(FOCUS):
        start = i * SLOT
        keys = ";".join(
            f"{v:.5f}" for v in (
                0, start / CYCLE, (start + FADE) / CYCLE,
                (start + HOLD) / CYCLE, (start + SLOT) / CYCLE, 1,
            )
        )
        # The first value is up from the first frame, not after the first fade:
        # a field that reads empty for half a second on every load looks broken,
        # and it is the state most screenshots and previews will catch.
        vals = "1;1;1;1;0;0" if i == 0 else "0;0;1;1;0;0"
        parts.append(
            f'<text x="{x}" y="{VALUE_Y}" font-family="{MONO}" font-size="14.5" '
            f'fill="{t["text"]}" opacity="{1 if i == 0 else 0}">{esc(value)}'
            f'<animate attributeName="opacity" dur="{CYCLE}s" repeatCount="indefinite" '
            f'values="{vals}" keyTimes="{keys}"/></text>'
        )
    return "".join(parts)


def build(theme: str) -> str:
    t = THEMES[theme]
    right = W - PAD

    # Status field is right-aligned against the same rule the name sits on, so
    # the two ends of the document line up rather than drifting.
    status = (
        f'<g opacity="1">'
        f'<animate attributeName="opacity" from="0" to="1" dur="0.5s" begin="0.85s" fill="freeze"/>'
        f'<text x="{right}" y="{FIELD_Y}" text-anchor="end" font-family="{MONO}" '
        f'font-size="10.5" letter-spacing="2.6" fill="{t["faint"]}">STATUS</text>'
        f'<text x="{right}" y="{VALUE_Y}" text-anchor="end" font-family="{MONO}" '
        f'font-size="14.5" fill="{t["text"]}">open to work</text>'
        f'<circle cx="{right - 128}" cy="{VALUE_Y - 5}" r="3.5" fill="{t["brass"]}">'
        f'<animate attributeName="opacity" values="1;0.25;1" dur="2.6s" '
        f'repeatCount="indefinite"/></circle>'
        f'</g>'
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"
     viewBox="0 0 {W} {H}" role="img"
     aria-label="Nolwen Sean Hononta, fullstack engineer. Focus: fullstack product work from interface to chain; agent payment rails, x402 and MPP; onchain settlement and ERC-8004 verdicts. Status: open to work.">
  <title>Nolwen Sean Hononta</title>

  <rect width="{W}" height="{H}" fill="{t['ground']}"/>

  <!-- The brass edge. One accent in the whole asset, and it is a margin rule
       rather than a decorative rail: it marks where the document begins. -->
  <rect x="0" y="0" width="4" height="{H}" fill="{t['brass']}">
    <animate attributeName="opacity" values="0;1" dur="0.6s" fill="freeze"/>
  </rect>

  <text x="{PAD}" y="{BASE_NAME}" font-family="{SANS}" font-size="52"
        font-weight="800" letter-spacing="-1.6" fill="{t['text']}">{esc(NAME)}</text>

  <!-- The rule draws once, left to right, and then the page is still. -->
  <rect x="{PAD}" y="{RULE_Y}" width="{W - PAD * 2}" height="1" fill="{t['rule']}">
    <animate attributeName="width" from="0" to="{W - PAD * 2}" dur="0.9s"
             fill="freeze" calcMode="linear"
             values="0;{W - PAD * 2};{W - PAD * 2}" keyTimes="0;0.6;1"/>
  </rect>

  {field(PAD, "REF", REF, t, 0.35)}
  {focus_field(PAD + 250, t)}
  {status}
</svg>
"""


def main() -> None:
    out = Path(__file__).resolve().parent.parent / "assets"
    out.mkdir(exist_ok=True)
    for theme in THEMES:
        path = out / f"header-{theme}.svg"
        path.write_text(build(theme), encoding="utf-8")
        print(f"  wrote assets/{path.name} ({path.stat().st_size / 1024:.1f} kB)")

    widest = max(len(v) for v in FOCUS) * 14.5 * MONO_ADV
    end = PAD + 250 + widest
    print(f"  FOCUS cycle {CYCLE:.1f}s; widest value ends at {end:.0f}px of {W}")
    if end > W - PAD - 150:
        raise SystemExit("FOCUS value collides with the STATUS column")


if __name__ == "__main__":
    main()
