from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from bs4 import element


class PySide6FuncDescription:
    """Класс описание функции"""
    def __init__(self, raw: "element.Tag") -> None:
        """Инициализация

        Args:
            raw (element.Tag): Описание функции с сайта
        """
        self.raw = raw

    @property
    def text(self) -> str:
        """Неформатированное описание функции с сайта."""
        return self.raw.text
