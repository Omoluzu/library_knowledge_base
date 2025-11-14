
from PySide6.QtWidgets import (
    QWidget,
    QListWidget,
)


class NameClassWidget(QWidget):
    """Обертка над QListWidget для показа наименований всех классов,
    заведенных в DB"""

    def __init__(self) -> None:
        from .connect import set_connect
        from .ui import set_ui

        super().__init__()

        self.list_widget = QListWidget()

        set_ui(self)
        set_connect(self)
