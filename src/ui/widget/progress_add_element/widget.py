from typing import Any

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QProgressBar, QPushButton
)


class ProgressAddElementWidget(QWidget):
    """UI для прогресса добавления новых элементов"""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация"""
        super().__init__(*args, **kwargs)

        self.name_upload_element = QLabel()
        self.progress = QProgressBar()
        self.close_btn = QPushButton("x", self)
        self.wrapper = QWidget()

        self.setConfig()
        self.setupUI()

    def setConfig(self) -> None:
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setFixedSize(360, 72)
        self.setStyleSheet(
            """background-color:transparent;
            border-radius:10px;
        """)

        self.wrapper.setStyleSheet(
            """background-color:#294250;
            border-radius:10px;
            border:1px solid #04304A
        """)

        self.name_upload_element.setFixedSize(360, 42)
        self.name_upload_element.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_upload_element.setStyleSheet(
            """background-color:#D7E4C8;
            border-bottom-left-radius:0px;
            border-bottom-right-radius:0px;
            font-size:32px;
            font-family:Agave Nerd Font;
            padding-top:5px;
        """)

        self.progress.setTextVisible(False)
        self.progress.setFixedSize(360, 19)
        self.progress.setStyleSheet(
            """
            QProgressBar {
                background-color: transparent;
                border:1px solid transparent;
            }
            QProgressBar:chunk {
                background-color: #86C444;
                border-bottom-left-radius:10px;
            }
        """)

        self.close_btn.setFixedSize(24, 24)
        self.close_btn.move(
            (self.width() // 2) - (self.close_btn.width() // 2),
            self.height() - (self.close_btn.height())
        )
        self.close_btn.setStyleSheet(
            """background-color: #B53C3C;
            border:2px solid #5C0404;
            border-radius:8px;
            font-size:25px;
            font-family:Agave Nerd Font;
        """)

    def setupUI(self) -> None:
        wrapper_layer = QVBoxLayout(self.wrapper)
        wrapper_layer.addWidget(self.name_upload_element)
        wrapper_layer.addWidget(self.progress)
        wrapper_layer.setContentsMargins(0, 0, 0, 0)
        wrapper_layer.setSpacing(0)

        layer = QVBoxLayout(self)
        layer.addWidget(self.wrapper)
        layer.addStretch()
        layer.setContentsMargins(0, 0, 0, 0)
        layer.setSpacing(0)

        self.close_btn.raise_()
