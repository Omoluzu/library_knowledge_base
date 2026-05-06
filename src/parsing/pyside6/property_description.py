from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from bs4 import element


class PySide6PropertyDescription:
    """Работа с описанием элемента Property"""
    def __init__(self, raw: "element.Tag") -> None:
        """Инициализация

        Args:
            raw (element.Tag): Неформатированные HTML данные
        """
        self.raw = raw

    @property
    def text(self) -> str:
        """Содержимое описания

        Args:
            str: Описание
        """
        return self.raw.text
