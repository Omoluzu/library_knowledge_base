from typing import List

from PySide6.QtCore import Slot, Signal

from db import models
from .widget import NameFuncWidget
from .elements import FuncItemWidget


class NameFunc(NameFuncWidget):
    """Обертка над QListWidget для показа наименований функций,
    выбранного класса """
    __slot__ = ('list_widget',)

    # Этот сигнал испускается с указанным элементом, когда кнопка мыши
    #  нажимается по элементу в виджете.
    itemClicked = Signal(models.page.PageFunc)

    def addItem(self, items: List[models.page.PageFunc]) -> None:
        """Вставьте элемент с текстовой меткой в ​​конце виджета списка.

        Args:
            items: Список моделей PageFunc.
        """
        self.list_widget.clear()
        for func in items:
            self.list_widget.addItem(FuncItemWidget(func))

    @Slot(FuncItemWidget)
    def slot_item_clicked(self, item: FuncItemWidget) -> None:
        """Слот получающий сигнал, когда кнопка мыши нажимается по элементу в
        виджете.

        Args:
            item: QListWidgetItem, элемента по которому был нажата кнопка мыши.
        """
        self.itemClicked.emit(item.db_model)
