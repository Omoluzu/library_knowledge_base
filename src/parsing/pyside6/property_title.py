from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from bs4 import element


class PySide6PropertyTitle:
    """Работа с заголовком элемента Property"""
    def __init__(self, raw: "element.Tag") -> None:
        """Инициализация

        Args:
            raw (element.Tag): Неформатированные HTML данные
        """
        self.raw = raw

    def __str__(self) -> str:
        return self.name

    @property
    def name(self) -> str:
        """Получение наименование property

        Args:
            str: Наименование
        """
        return self.raw.text.split(' : ')[0]
