from typing import Any

from db import models
from repository import db

from .widget import PySide6Widget


class PySide6(PySide6Widget):
    """Основной виджет для работы с PySide6 документацией"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация"""
        super().__init__(*args, **kwargs)

        self._repo_page = db.DBPageRepository()

        self.setConfig()
        self.setConnect()

    def refresh_pages(self) -> None:
        """Обновление данных виджета"""
        self.pages_widget.clear()
        self.pages_widget.addItems(
            self._repo_page.get_all())
        self.pages_widget.update()

    def refresh_func(self) -> None:
        """Обновление данных функций"""
        current_pages_name = self.pages_widget.currentItem().text()
        model_pages = self._repo_page.get(current_pages_name)
        self.slot_item_clicked(model_pages)

    # TODO: Слоты не слоты
    def slot_filter_text_changed(self, text: str) -> None:
        """Слот на изменение текста в поле фильтра

        Args:
            text (str): Введенный текст
        """
        self.refresh_func()

    def slot_item_clicked(self, item: models.page.Page) -> None:
        """Клик по наименованию виджет

        Args:
            item (models.page.Page): TODO:
        """
        self.func_widget.addItem(item.func, filter_text=self.filter.text())

        text = (
            f"{item.title.removesuffix(' Class')}({item.inherits})"
            f"\n\n{str(item.description_ru)}"
        )

        self.description_widget.setText(text)

    def slot_item_deleter(self, item: models.page.Page) -> None:
        """TODO:

        Args:
            item (models.page.Page): TODO:
        """
        self._repo_page.remove(item)
        self.refresh_pages()

    def slot_item_open(self, item: models.page.Page) -> None:
        """TODO:

        Args:
            item (models.page.Page): TODO:
        """
        print("slot_item_open", item)

    def slot_func_item_clicked(
            self, item: models.page.PageFunc) -> None:
        """Клик по наименование метода"""
        self.description_widget.clear()

        text = (
            f"{item.name}({item.raw_args}) -> {item.raw_returns}"
            f"\n\n{item.description_ru}"
        )
        self.description_widget.setText(text)

    def setConfig(self) -> None:
        self.pages_widget.addItems(self._repo_page.get_all())

        total = self.height()
        self.main_splitter.setSizes(  # type: ignore
            [int(total * 0.2), int(total * 0.2), int(total * 0.6)])

    def setConnect(self) -> None:
        self.pages_widget.itemClicked.connect(self.slot_item_clicked)
        self.pages_widget.itemDeleter.connect(self.slot_item_deleter)
        self.pages_widget.itemOpen.connect(self.slot_item_open)
        self.func_widget.itemClicked.connect(self.slot_func_item_clicked)
        self.filter.textChanged.connect(self.slot_filter_text_changed)
