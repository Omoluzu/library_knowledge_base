import enum
from typing import Any, Optional, TYPE_CHECKING

from PySide6.QtWidgets import QMenu


if TYPE_CHECKING:
    from .class_item import TitleClassItemWidget


class NameClassMenu(QMenu):
    """TODO: """

    class ActionName(enum.Enum):
        deleter = "Удалить"
        open = "Открыть"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация"""
        super().__init__(*args, **kwargs)

        self.clicked_item: Optional["TitleClassItemWidget"] = None

        for action_name in self.ActionName:
            self.addAction(action_name.value)
