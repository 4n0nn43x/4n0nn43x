#!/usr/bin/env python3
"""Generate the animated profile header, once per theme.

Why a generator and not two hand-written SVGs: the dark and light headers are
the same drawing with a different palette, and two hand-maintained copies drift
the moment one is edited. Here the geometry and the timing exist once.

Why SMIL rather than CSS keyframes: GitHub serves README images through its
camo proxy, which hands the browser the raw bytes as an image. SVG rendered as
an image runs SMIL reliably everywhere; CSS animation support inside
image-context SVG is the part that varies between renderers.

Run:  python3 tools/make-header.py
"""

from pathlib import Path

# Three phrases, typed then erased, forever. Keep them short: the caret has to
# land inside the banner at the widest phrase, not past its edge.
PHRASES = [
    "AI agents that put money behind their claims",
    "x402 payments, ERC-8004 reputation, onchain",
    "solo builds, shipped to production",
]

TYPE_S = 1.4   # typing
HOLD_S = 2.0   # phrase fully visible
ERASE_S = 0.5  # erasing
SLOT = TYPE_S + HOLD_S + ERASE_S
CYCLE = SLOT * len(PHRASES)

W, H = 1000, 230

THEMES = {
    "dark": {
        "bg0": "#0b1020", "bg1": "#131a33", "bg2": "#0d1226",
        "name": "#f2f5ff", "accent0": "#7c5cff", "accent1": "#22d3ee",
        "muted": "#8b94b8", "dot": "#2a3358", "type": "#c9d2f5",
    },
    "light": {
        "bg0": "#f6f7fb", "bg1": "#eceffb", "bg2": "#f9fafe",
        "name": "#0d1226", "accent0": "#5b3df5", "accent1": "#0891b2",
        "muted": "#5b6488", "dot": "#d7ddf0", "type": "#28304f",
    },
}

MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Inter,Roboto,Helvetica,Arial,sans-serif"


def dots(colour: str) -> str:
    """A faint dot grid, plus a few that breathe.

    The grid is a `<pattern>` rather than ~170 `<circle>` elements: tiled once
    by the renderer instead of animated individually. The first version drew
    every dot and animated each one, which cost 36 kB and put 170 concurrent
    SMIL timelines on screen for an effect nobody consciously sees. Nine
    hand-placed dots carry the same impression of life.
    """
    breathing = "".join(
        f'<circle cx="{x}" cy="{y}" r="1.6" fill="{colour}">'
        f'<animate attributeName="opacity" values="0.15;0.85;0.15" '
        f'dur="{dur}s" begin="{begin}s" repeatCount="indefinite"/></circle>'
        for x, y, dur, begin in (
            (126, 44, 5, 0.0), (262, 196, 6, 1.3), (398, 30, 4.5, 2.1),
            (534, 210, 5.5, 0.7), (676, 52, 6.5, 1.9), (742, 168, 4.8, 3.0),
            (868, 36, 5.2, 2.4), (930, 132, 6.1, 0.4), (612, 118, 5.8, 3.4),
        )
    )
    return (
        f'<defs><pattern id="grid" width="34" height="34" patternUnits="userSpaceOnUse">'
        f'<circle cx="2" cy="2" r="1.1" fill="{colour}"/></pattern></defs>'
        f'<rect width="{W}" height="{H}" fill="url(#grid)" opacity="0.45"/>'
        f'{breathing}'
    )


def typed_line(index: int, text: str, t: dict) -> str:
    """One phrase: revealed by a clip rect, erased the same way, then silent.

    Each phrase owns a slot in the loop and is invisible outside it, so all
    three can share the same baseline without ever overlapping.
    """
    start = index * SLOT
    char_w = 10.6           # 17px monospace, measured rather than guessed
    full = len(text) * char_w
    cid = f"clip{index}"

    # Visible only during its own slot.
    vis = (
        f'<set attributeName="opacity" to="1" begin="{start}s"/>'
        f'<set attributeName="opacity" to="0" begin="{start + SLOT}s"/>'
    )

    reveal = (
        f'<animate attributeName="width" from="0" to="{full}" dur="{TYPE_S}s" '
        f'begin="{start}s" fill="freeze" calcMode="discrete" '
        f'values="{";".join(str(round(full * i / len(text), 1)) for i in range(len(text) + 1))}"/>'
        f'<animate attributeName="width" from="{full}" to="0" dur="{ERASE_S}s" '
        f'begin="{start + TYPE_S + HOLD_S}s" fill="freeze"/>'
    )

    # The caret rides the end of the revealed span, then blinks while holding.
    caret = (
        f'<rect y="0" width="2" height="24" fill="{t["accent1"]}" opacity="0">'
        f'{vis}'
        f'<animate attributeName="x" from="0" to="{full}" dur="{TYPE_S}s" '
        f'begin="{start}s" fill="freeze"/>'
        f'<animate attributeName="x" from="{full}" to="0" dur="{ERASE_S}s" '
        f'begin="{start + TYPE_S + HOLD_S}s" fill="freeze"/>'
        f'<animate attributeName="opacity" values="1;0;1" dur="1s" '
        f'begin="{start + TYPE_S}s" repeatCount="{int(HOLD_S)}"/>'
        f'</rect>'
    )

    return (
        f'<defs><clipPath id="{cid}"><rect x="0" y="0" width="0" height="30">'
        f'{reveal}</rect></clipPath></defs>'
        f'<g transform="translate(58,150)" opacity="0">{vis}'
        f'<g clip-path="url(#{cid})">'
        f'<text x="0" y="19" font-family="{MONO}" font-size="17" '
        f'fill="{t["type"]}">{text}</text></g>'
        f'<g transform="translate(0,-1)">{caret}</g>'
        f'</g>'
    )


def build(theme: str) -> str:
    t = THEMES[theme]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}"
     viewBox="0 0 {W} {H}" role="img"
     aria-label="Nolwen Sean Hononta - AI agents and onchain systems">
  <title>Nolwen Sean Hononta</title>
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="{t['bg0']}"/>
      <stop offset="50%" stop-color="{t['bg1']}"/>
      <stop offset="100%" stop-color="{t['bg2']}"/>
      <animate attributeName="x1" values="0;0.4;0" dur="14s" repeatCount="indefinite"/>
      <animate attributeName="y2" values="1;0.6;1" dur="14s" repeatCount="indefinite"/>
    </linearGradient>

    <linearGradient id="accent" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{t['accent0']}"/>
      <stop offset="100%" stop-color="{t['accent1']}"/>
    </linearGradient>

    <!-- The aurora: two slow blurred blobs. All the life in the banner comes
         from these, which is why they move on different periods - equal periods
         would beat in sync and read as a loop. -->
    <filter id="soft" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="46"/>
    </filter>

    <clipPath id="card"><rect width="{W}" height="{H}" rx="18"/></clipPath>
  </defs>

  <g clip-path="url(#card)">
    <rect width="{W}" height="{H}" fill="url(#bg)"/>

    <g filter="url(#soft)" opacity="0.5">
      <circle cx="180" cy="60" r="120" fill="{t['accent0']}">
        <animate attributeName="cx" values="180;340;180" dur="17s" repeatCount="indefinite"/>
        <animate attributeName="cy" values="60;150;60" dur="21s" repeatCount="indefinite"/>
      </circle>
      <circle cx="820" cy="180" r="110" fill="{t['accent1']}">
        <animate attributeName="cx" values="820;660;820" dur="23s" repeatCount="indefinite"/>
        <animate attributeName="cy" values="180;70;180" dur="19s" repeatCount="indefinite"/>
      </circle>
    </g>

    <g opacity="0.55">{dots(t['dot'])}</g>

    <text x="58" y="94" font-family="{SANS}" font-size="44" font-weight="700"
          fill="{t['name']}" letter-spacing="-0.5">Nolwen Sean Hononta</text>

    <text x="58" y="122" font-family="{MONO}" font-size="13"
          fill="{t['muted']}" letter-spacing="2.4">ENGINEER / AI AGENTS / ONCHAIN</text>

    {"".join(typed_line(i, p, t) for i, p in enumerate(PHRASES))}

    <!-- Accent rule, drawn once on load rather than looping: the eye should
         settle on the typing, not on a second thing competing with it. -->
    <rect x="58" y="196" width="0" height="3" rx="1.5" fill="url(#accent)">
      <animate attributeName="width" from="0" to="240" dur="1.1s" fill="freeze"/>
    </rect>
  </g>
</svg>
"""


def main() -> None:
    out = Path(__file__).resolve().parent.parent / "assets"
    out.mkdir(exist_ok=True)
    for theme in THEMES:
        path = out / f"header-{theme}.svg"
        path.write_text(build(theme), encoding="utf-8")
        print(f"  wrote {path.relative_to(path.parent.parent)} ({path.stat().st_size // 1024} kB)")
    print(f"  loop: {CYCLE:.1f}s over {len(PHRASES)} phrases")


if __name__ == "__main__":
    main()
