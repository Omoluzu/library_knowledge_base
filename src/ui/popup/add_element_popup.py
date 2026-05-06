
from typing import Any, TYPE_CHECKING

from PySide6.QtWidgets import (
    QWidget,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QProgressBar,
)
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPalette, QColor


if TYPE_CHECKING:
    from PySide6.QtGui import QKeyEvent, QShowEvent

    from src.ui.widget.main import MainCentralWidget


class AddElementPopup(QWidget):
    """TODO: """

    app_width: int = 400
    """Ширина виджета"""

    addElement = Signal(str)
    """Сигнал на добавление нового элемента"""

    def __init__(
            self, parent: "MainCentralWidget", *args: Any, **kwargs: Any
    ) -> None:
        """TODO:

        Args:
            parent (MainCentralWidget): TODO:
        """
        super().__init__(parent, *args, **kwargs)

        self.app = parent
        self.setGeometry(0, 0, parent.width(), parent.height())

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(0, 0, 0, 150))
        self.setPalette(palette)

        self.popup_content = QWidget(self)
        self.popup_content.setStyleSheet(
            """background-color:#294250; border-radius:10px;
            border:1px solid #04304a;
            font-size:22px; font-family:Agave Nerd Font;"""
        )
        self.popup_content.setGeometry(
            (self.width() - self.app_width) // 2, (self.height() - 200) // 2,
            self.app_width, 200)

        self.input_line_edit = QLineEdit(
            placeholderText="qwidget", parent=self.popup_content)
        self.input_line_edit.setFixedSize(self.popup_content.width() - 40, 40)
        self.input_line_edit.setStyleSheet(
            """background-color:#d7e4c8""")
        self.input_line_edit.setFocus()

        self.progress = QProgressBar()
        self.progress.setStyleSheet("""border-radius: 0px;""")

        close_button = QPushButton("X", self.popup_content)
        close_button.setFixedSize(self.app_width // 5, 50)
        close_button.clicked.connect(self.slot_close_popup)
        close_button.setStyleSheet(
            """background-color: #b53c3c; border-radius:0px;
            border-bottom-left-radius:10px; border:1px solid #5c0404;
            color: #c4a3a3;""")

        run_button = QPushButton("-->", self.popup_content)
        run_button.setFixedHeight(50)
        run_button.clicked.connect(self.slot_add_element)
        run_button.setStyleSheet(
            """background-color:#86c444; color:#d7e4c8;
            border-radius:0px; border:1px solid #11242f;
            border-bottom-right-radius:10px;
            """)

        layer_control_button = QHBoxLayout()
        layer_control_button.addWidget(close_button)
        layer_control_button.addWidget(run_button)

        layer = QVBoxLayout(self.popup_content)
        layer.setContentsMargins(0, 0, 0, 0)
        layer.setSpacing(0)
        layer.addWidget(
            self.input_line_edit, alignment=Qt.AlignmentFlag.AlignCenter)
        layer.addWidget(self.progress)
        layer.addLayout(layer_control_button)

    def showEvent(self, event: "QShowEvent") -> None:
        self.setGeometry(0, 0, self.app.width(), self.app.height())
        self.popup_content.setGeometry(
            (self.width() - self.app_width) // 2, (self.height() - 200) // 2,
            self.app_width, 200)

        self.input_line_edit.clear()
        self.input_line_edit.setFocus()

        self.progress.reset()
        super().showEvent(event)

    def slot_add_element(self) -> None:
        """Отработка сигнала нажатия на кнопку add"""
        self.addElement.emit(self.input_line_edit.text().lower())

    def slot_close_popup(self) -> None:
        """TODO:"""
        self.hide()

    def keyPressEvent(self, event: "QKeyEvent") -> None:
        if event.key() == Qt.Key.Key_Return:
            self.slot_add_element()
        elif event.key() == Qt.Key.Key_Escape:
            self.slot_close_popup()

        super().keyPressEvent(event)
