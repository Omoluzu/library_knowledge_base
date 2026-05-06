from typing import Any


from PySide6.QtWidgets import QWidget, QListWidget, QHBoxLayout

from .elements.class_menu_item import NameClassMenu


class NameClassWidget(QWidget):
    """Обертка над QListWidget для показа наименований всех классов,
    заведенных в DB"""
    __slots__ = ("list_widget", )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.list_widget = QListWidget()
        """QList для вывода списка наименований классов PySide6"""

        self.menu = NameClassMenu(self)
        """TODO:"""

        self.setupUI()

    def setupUI(self) -> None:
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.list_widget)

        self.setLayout(main_layout)
