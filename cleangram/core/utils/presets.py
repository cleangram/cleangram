from dataclasses import dataclass
from typing import Optional


@dataclass
class Presets:
    parse_mode: Optional[str] = None
    disable_web_page_preview: Optional[bool] = None
