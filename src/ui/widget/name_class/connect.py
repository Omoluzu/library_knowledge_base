from .widget import NameClassWidget


def set_connect(self: NameClassWidget) -> None:
    self.list_widget.itemClicked.connect(self.slot_item_clicked)
