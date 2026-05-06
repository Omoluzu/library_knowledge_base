from typing import List, TYPE_CHECKING

from .page_func_title import PySide6FuncTitle
from .page_func_description import PySide6FuncDescription


if TYPE_CHECKING:
    from bs4 import element
    from parsing.pyside6 import QFRFaqPage


class PySide6WidgetFunc:
    """Парсинг выбранной функции класса"""
    def __init__(self, parent: "QFRFaqPage", raw_name: "element.Tag") -> None:
        """Инициализация

        Args:
            parent (QFRFaqPage): Родительский класс функции
            raw_name (str): HTML с наименованием функции
        """
        self.parent = parent
        self.name = PySide6FuncTitle(
            title_class_name=parent.title.name, raw=raw_name)
        self.description: List[PySide6FuncDescription] = []

    def append_description_raw(self, raw_description: "element.Tag") -> None:
        """Добавление описания к функции

        Args:
            raw_description (element.Tab): HTML абзац с описанием.
        """
        self.description.append(PySide6FuncDescription(raw=raw_description))
