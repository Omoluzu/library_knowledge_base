
from bs4 import element


class PySide6Title:
    """Работа с заголовком класса PySide6"""
    def __init__(self, raw: element.Tag) -> None:
        """Инициализация

        Args:
            raw (element.Tag): Данные заголовка с сайта
        """
        self.raw = raw
        """Данные заголовка с сайта"""

    def __call__(self) -> str:
        return self.name

    @property
    def name(self) -> str:
        """Получение наименования заголовка

        Returns:
            str: Строковое представление наименования заголовка
        """
        return self.raw.text.removesuffix("Class").strip()
