from dataclasses import dataclass

from .parse_mode import ParseMode


@dataclass
class Presets:
    parse_mode: ParseMode
