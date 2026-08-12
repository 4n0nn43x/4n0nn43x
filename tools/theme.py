"""Palette and type, shared by every asset generator here.

Direction: a settlement record, not a hero banner.

The first pass of this profile went straight to the house style of machine-made
design - purple-to-cyan gradient, blurred aurora blobs, a dot grid, rounded
cards with an accent rail, content in pills. Every one of those is on the list
of things that read as generated, and using three of them at once is why the
result looked like every other page.

So the vocabulary here comes from the subject instead. The work is bonded
execution: an agent signs a commitment, money is held against it, and a verdict
is recorded. That world has a visual language already - labelled fields, hairline
rules, values set in a face that keeps its columns, one seal. Square corners,
because a document has square corners.

Brass rather than an accent hue: it is the colour of a seal and of a coin, it is
warm without being the terracotta every generated page reaches for, and there is
exactly one of it per asset.

Contrast is a constraint here, not an afterthought. The first version of this
palette put the field labels at 2.56:1 on the dark ground - below the floor even
for large text, at 10.5px. Every text tone below now clears 4.5:1 against its own
ground, checked in both themes; the hairlines sit deliberately under that because
a rule that meets text contrast stops being a hairline and starts being a border.
"""

THEMES = {
    "dark": {
        "ground": "#16130F",     # warm ink, not slate, not GitHub's #0d1117
        "field": "#1E1A15",      # raised surface, barely
        "rule": "#554B3F",       # hairlines
        "ruleSoft": "#453C31",
        "text": "#E6DFD3",       # warm bone
        "muted": "#B8AC99",
        "faint": "#8A8070",
        "brass": "#C9962B",
    },
    "light": {
        "ground": "#EFEDE6",
        "field": "#E7E4DA",
        "rule": "#BDB5A3",
        "ruleSoft": "#CFC7B6",
        "text": "#1A1712",
        "muted": "#4F4739",
        "faint": "#6B6254",
        "brass": "#9A6E12",      # darkened so it holds on paper
    },
}

# System stacks. A webfont cannot be linked from an SVG that GitHub serves
# through its image proxy, and embedding a face as base64 would cost more bytes
# than the whole asset. The personality has to come from scale, weight and
# spacing instead of from an exotic family - which is the harder discipline and
# the one that survives on someone else's machine.
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"
SANS = ("Inter,-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,"
        "'Helvetica Neue',Arial,sans-serif")

MONO_ADV = 0.601   # advance per char, as a fraction of font-size, for the stack above


def esc(text: str) -> str:
    """XML-escape. `C++` and `A & B` would otherwise produce invalid SVG."""
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
