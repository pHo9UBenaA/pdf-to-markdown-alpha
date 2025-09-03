"""Type stubs for markdownify module."""

from typing import Optional

def markdownify(
    html: str,
    *,
    heading_style: str = "underlined",
    strip: Optional[str] = None,
    convert: Optional[list[str]] = None,
    autolinks: bool = True,
    default_title: bool = False,
    escape_asterisks: bool = True,
    escape_underscores: bool = True,
    escape_misc: bool = True,
    wrap: bool = False,
    wrap_width: int = 80,
    newline_style: str = "native",
    code_language: str = "",
) -> str: ...
