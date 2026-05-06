from typing import Any


from PySide6.QtWidgets import (
    QWidget,
    QTextEdit,
    QSplitter,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
)


from . import elements


class PySide6Widget(QWidget):
    """UI отображения основного виджета PySide6 документации"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация"""
        super().__init__(*args, **kwargs)

        self.pages_widget = elements.NameClassWidget()
        """TODO:"""
        self.filter = QLineEdit('')
        """TODO:"""
        self.func_widget = elements.NameFuncWidget()
        """TODO:"""
        self.description_widget = QTextEdit()
        """TODO:"""
        self.main_splitter = QSplitter()
        """TODO:"""

        self.setupUI()

    def setupUI(self) -> None:
        func_widget_substrate = QWidget()
        func_layout = QVBoxLayout(func_widget_substrate)
        func_layout.addWidget(self.filter)
        func_layout.addWidget(self.func_widget)

        self.main_splitter.addWidget(self.pages_widget)
        self.main_splitter.addWidget(func_widget_substrate)
        self.main_splitter.addWidget(self.description_widget)

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.main_splitter)
        self.setLayout(main_layout)
