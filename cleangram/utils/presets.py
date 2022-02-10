from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Presets:
    _parse_mode: Optional[str] = field(default=None)
    _disable_web_page_preview: Optional[bool] = field(default=None)
    _allow_sending_without_reply: Optional[bool] = field(default=None)
    _disable_notification: Optional[bool] = field(default=None)
    _protect_content: Optional[bool] = field(default=None)

    def __getattr__(self, item):
        def _(obj):
            if getattr(obj, item) is None:
                setattr(obj, item, getattr(self, f"_{item}"))

        return _
