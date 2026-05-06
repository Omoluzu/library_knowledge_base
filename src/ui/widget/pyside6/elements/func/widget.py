from typing import Any

from PySide6.QtWidgets import QWidget, QListWidget, QHBoxLayout


class NameFuncWidget(QWidget):
    """Обертка над QListWidget для показа наименований функций,
    выбранного класса """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация"""
        super().__init__()

        self.list_widget = QListWidget()
        """QListWidget для показа функций"""

        self.setupUI()

    def setupUI(self) -> None:
        main_layout = QHBoxLayout()
        main_layout.addWidget(self.list_widget)

        self.setLayout(main_layout)
