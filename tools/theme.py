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
"""

THEMES = {
    "dark": {
        "ground": "#16130F",     # warm ink, not slate, not GitHub's #0d1117
        "field": "#1E1A15",      # raised surface, barely
        "rule": "#3A3229",       # hairlines
        "ruleSoft": "#2A241D",
        "text": "#E6DFD3",       # warm bone
        "muted": "#9A8F7F",
        "faint": "#5E564A",
        "brass": "#C9962B",
    },
    "light": {
        "ground": "#EFEDE6",
        "field": "#E7E4DA",
        "rule": "#CFC9BB",
        "ruleSoft": "#DEDACE",
        "text": "#1A1712",
        "muted": "#6B6254",
        "faint": "#A79D8C",
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
