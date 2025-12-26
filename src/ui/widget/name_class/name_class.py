from typing import List

from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtCore import Slot, Signal

from db import models

from .widget import NameClassWidget
from .elements.class_item import TitleClassItemWidget


class NameClass(NameClassWidget):
    """Обертка над QListWidget для показа наименований всех классов,
    заведенных в DB"""
    __slot__ = ('list_widget')

    itemClicked = Signal(models.page.Page)

    def addItem(
            self, items: List[models.page.Page], filter_text: str = ''
    ) -> None:
        """Вставьте элемент с текстовой меткой в ​​конце виджета списка.

        Args:
            items (List[models.page.Page]): Список моделей Page.
            filter (str): Фильтр отображения текста
        """
        for name_class in items:
            self.list_widget.addItem(TitleClassItemWidget(name_class))

    def clear(self) -> None:
        """Удаляет все элементы и выборки в представлении."""
        self.list_widget.clear()

    def currentItem(self) -> QListWidgetItem:
        """Возвращает текущий элемент.

        Returns:
            QListWidgetItem: QListWidgetItem
        """
        return self.list_widget.currentItem()

    @Slot(TitleClassItemWidget)
    def slot_item_clicked(self, item: TitleClassItemWidget) -> None:
        """Слот получающий сигнал, когда кнопка мыши нажимается по элементу в
        виджете.

        Args:
            item: QListWidgetItem, элемента по которому был нажата кнопка мыши.
        """
        self.itemClicked.emit(item.page)
