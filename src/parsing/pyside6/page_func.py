
from .page_func_title import PySide6FuncTitle


class QFRFaqPageFuncDescription:
    def __init__(self, parent: object, raw: str) -> None:
        self.parent = parent
        self.raw = raw

    @property
    def text(self) -> str:
        return self.raw.text


class QFRFaqPageFunc:
    def __init__(self, parent: object, raw_name: str) -> None:
        """Инициализация

        Args:
            raw_name: HTML с наименованием функции
        """
        self.parent = parent
        self.name = PySide6FuncTitle(parent=parent, raw=raw_name)
        self.description = []

    def append_description_raw(self, raw_description: str) -> None:
        """Добавление описания к функции

        Args:
            raw_description: HTML абзац с описанием.
        """
        self.description.append(
            QFRFaqPageFuncDescription(parent=self.parent, raw=raw_description))
