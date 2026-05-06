from typing import List, Any

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QListWidgetItem
from PySide6.QtCore import Slot, Signal, Qt, QPoint

from db import models

from .widget import NameClassWidget
from .elements.class_item import TitleClassItemWidget


class NameClass(NameClassWidget):
    """Обертка над QListWidget для показа наименований всех классов,
    заведенных в DB"""

    itemClicked = Signal(models.page.Page)
    """TODO:"""

    itemDeleter = Signal(models.page.Page)
    """TODO:"""

    itemOpen = Signal(models.page.Page)
    """TODO:"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация"""
        super().__init__(*args, **kwargs)

        self.setConfig()

    def addItems(
            self, items: List[models.page.Page]
    ) -> None:
        """Вставьте элемент с текстовой меткой в ​​конце виджета списка.

        Args:
            items (List[models.page.Page]): Список моделей Page.
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
        self.itemClicked.emit(item.model_page)

    @Slot()
    def slot_show_context_menu(self, position: QPoint) -> None:
        """TODO:

        Args:
            position (QPoint): _description_
        """
        item = self.list_widget.itemAt(position)

        if isinstance(item, TitleClassItemWidget):
            self.menu.clicked_item = item
            self.menu.popup(self.list_widget.mapToGlobal(position))

    def slot_menu_triggered(self, action: QAction) -> None:
        """TODO:

        Args:
            action (QAction): _description_
        """
        action_name = self.menu.ActionName

        match action.text():
            case action_name.deleter.value:
                if (clicked_item := self.menu.clicked_item) is not None:
                    self.itemDeleter.emit(clicked_item.model_page)
                    self.menu.clicked_item = None
            case action_name.open.value:
                if (clicked_item := self.menu.clicked_item) is not None:
                    self.itemOpen.emit(clicked_item.model_page)
                    self.menu.clicked_item = None
            case _:
                pass

    def setConfig(self) -> None:
        self.list_widget.itemClicked.connect(self.slot_item_clicked)
        self.list_widget.customContextMenuRequested.connect(
            self.slot_show_context_menu)

        self.list_widget.setContextMenuPolicy(
            Qt.ContextMenuPolicy.CustomContextMenu)

        self.menu.triggered.connect(self.slot_menu_triggered)
