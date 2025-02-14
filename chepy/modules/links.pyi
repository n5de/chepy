from ..core import ChepyCore
from typing import Any, TypeVar

LinksT = TypeVar('LinksT', bound='Links')

class Links(ChepyCore):
    def __init__(self, *data: Any) -> None: ...
    state: Any = ...
    def pastebin_to_raw(self) -> LinksT: ...
    def github_to_raw(self) -> LinksT: ...
