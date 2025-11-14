from PySide6.QtWidgets import QHBoxLayout

from .widget import NameClassWidget


def set_ui(self: NameClassWidget) -> None:
    main_layout = QHBoxLayout()
    main_layout.addWidget(self.list_widget)

    self.setLayout(main_layout)
