from PySide6.QtWidgets import QWidget, QListWidget


class NameFuncWidget(QWidget):
    """Обертка над QListWidget для показа наименований функций,
    выбранного класса """

    def __init__(self) -> None:
        """Инициализация"""
        from .ui import set_ui
        from .connect import set_connect
        super().__init__()

        self.list_widget = QListWidget()

        set_connect(self)
        set_ui(self)
