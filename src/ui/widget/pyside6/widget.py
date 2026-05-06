from typing import Any


from PySide6.QtWidgets import (
    QWidget,
    QTextEdit,
    QSplitter,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
)


from ui import widget


class PySide6Widget(QWidget):
    """UI отображения основного виджета PySide6 документации"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация"""
        super().__init__(*args, **kwargs)

        self.pages_widget = widget.NameClassWidget()
        self.filter = QLineEdit('')
        self.func_widget = widget.func.NameFuncWidget()
        self.description_widget = QTextEdit()

        self.setupUI()

    def setupUI(self) -> None:

        func_widget_substrate = QWidget()
        func_layout = QVBoxLayout(func_widget_substrate)
        func_layout.addWidget(self.filter)
        func_layout.addWidget(self.func_widget)

        main_splitter = QSplitter()
        main_splitter.addWidget(self.pages_widget)
        main_splitter.addWidget(func_widget_substrate)
        main_splitter.addWidget(self.description_widget)

        main_layout = QHBoxLayout()
        main_layout.addWidget(main_splitter)
        self.setLayout(main_layout)
