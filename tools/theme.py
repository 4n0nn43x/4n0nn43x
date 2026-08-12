"""Palettes and type stacks, shared by every asset generator here.

Extracted the moment a second generator appeared. Two files each holding their
own copy of the same six hex values is a drift waiting to happen: the header
would be edited, the stack panel would not, and the profile would show two
palettes that are nearly-but-not-quite the same - the kind of wrongness a reader
feels without being able to name.
"""

THEMES = {
    "dark": {
        "bg0": "#0b1020", "bg1": "#131a33", "bg2": "#0d1226",
        "name": "#f2f5ff", "accent0": "#7c5cff", "accent1": "#22d3ee",
        "muted": "#8b94b8", "dot": "#2a3358", "type": "#c9d2f5",
        "pill": "#1a2244", "pillText": "#d7ddf5", "pillEdge": "#2f3a66",
    },
    "light": {
        "bg0": "#f6f7fb", "bg1": "#eceffb", "bg2": "#f9fafe",
        "name": "#0d1226", "accent0": "#5b3df5", "accent1": "#0891b2",
        "muted": "#5b6488", "dot": "#d7ddf0", "type": "#28304f",
        "pill": "#ffffff", "pillText": "#2b3350", "pillEdge": "#dbe1f2",
    },
}

MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Inter,Roboto,Helvetica,Arial,sans-serif"


def esc(text: str) -> str:
    """XML-escape. `C++` and `A & B` would otherwise produce invalid SVG."""
    return (
        text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    )
