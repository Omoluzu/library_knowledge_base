from typing import List, TYPE_CHECKING

from .property_title import PySide6PropertyTitle
from .property_description import PySide6PropertyDescription


if TYPE_CHECKING:
    from bs4 import element


class PySide6Property:
    """Работа с элементами property"""

    def __init__(self, raw_name: "element.Tag") -> None:
        """Инициализация

        Args:
            raw_name (element.Tag): HTML с наименованием атрибута
        """
        self.name = PySide6PropertyTitle(raw=raw_name)
        self.description: List[PySide6PropertyDescription] = []

    def append_description_raw(self, raw_description: "element.Tag") -> None:
        """Добавление описания атрибута

        Args:
            raw_description (element.Tag): HTML абзац с описанием.
        """
        self.description.append(
            PySide6PropertyDescription(raw=raw_description))
