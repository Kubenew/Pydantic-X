import re
import html
import unicodedata
from typing import Callable


class sanitize:
    """Built-in sanitizers (composable string functions)."""

    @staticmethod
    def trim(v: str) -> str:
        return v.strip()

    @staticmethod
    def lower(v: str) -> str:
        return v.lower()

    @staticmethod
    def upper(v: str) -> str:
        return v.upper()

    @staticmethod
    def collapse_spaces(v: str) -> str:
        return re.sub(r"\s+", " ", v).strip()

    @staticmethod
    def normalize_unicode(v: str) -> str:
        return unicodedata.normalize("NFKC", v)

    @staticmethod
    def strip_html(v: str) -> str:
        v = re.sub(r"<[^>]*>", "", v)
        return html.unescape(v)

    @staticmethod
    def max_len(n: int) -> Callable[[str], str]:
        def _f(v: str) -> str:
            return v[:n] if len(v) > n else v
        return _f
