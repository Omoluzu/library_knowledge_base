from .widget import NameFuncWidget


def set_connect(self: NameFuncWidget) -> None:
    self.list_widget.itemClicked.connect(self.slot_item_clicked)
