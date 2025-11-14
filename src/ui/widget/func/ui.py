from PySide6.QtWidgets import QHBoxLayout

from .widget import NameFuncWidget


def set_ui(self: NameFuncWidget) -> None:
    main_layout = QHBoxLayout()
    main_layout.addWidget(self.list_widget)

    self.setLayout(main_layout)
