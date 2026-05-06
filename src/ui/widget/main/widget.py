from typing import Any

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QResizeEvent
from PySide6.QtWidgets import QWidget, QTabWidget, QPushButton, QVBoxLayout

from ui import widget, popup


class MainCentralWidget(QWidget):
    """Центральный основной виджет"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация"""

        super().__init__(*args, **kwargs)

        self.pyside6_widget = widget.PySide6Widget()

        self.add_element_popup = popup.AddElementPopup(self)
        self.add_element_button = QPushButton('+')

        self.setConfig()
        self.setupUI()

    def setConfig(self) -> None:
        """Конфигурация"""
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)

        self.add_element_button.setFixedSize(QSize(40, 40))

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)

    def setupUI(self) -> None:
        """UI"""
        tabs = QTabWidget()
        tabs.addTab(self.pyside6_widget, "PySide6")

        # NOTE: Временно отключен OpenGL из-за отсутствия возможности развития
        # tabs.addTab(widget.OpenGLWidget(), "OpenGL")

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.add_element_button)
        main_layout.addWidget(tabs)
        self.setLayout(main_layout)
