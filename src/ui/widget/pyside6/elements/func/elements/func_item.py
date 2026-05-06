from typing import Any

from PySide6.QtWidgets import QListWidgetItem

from db import models


class FuncItemWidget(QListWidgetItem):
    """Отдельный элемент списка наименований функции."""

    def __init__(
            self, func: models.page.PageFunc, *args: Any, **kwargs: Any
    ) -> None:
        """Инициализация

        Args:
            func (models.page.PageFunc): Модель функции из базы данных
        """
        super().__init__()
        self.setText(str(func.name))
        self.db_model = func
        """Модель функции из базы данных"""
