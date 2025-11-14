from PySide6.QtWidgets import QListWidgetItem

from db import models


class FuncItemWidget(QListWidgetItem):
    """Отдельный элемент списка наименований функции.

    Attributes:
        db_model. Модель функции из базы данных.
    """

    def __init__(self, func: models.page.PageFunc) -> None:
        """Инициализация

        Args:
            func - Модель функции из базы данных
        """
        super().__init__(func.name)
        self.db_model = func
