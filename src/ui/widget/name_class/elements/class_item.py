from PySide6.QtWidgets import QListWidgetItem

from db import models


class TitleClassItemWidget(QListWidgetItem):
    """Отдельный элемент списка наименований классов.

    Attributes:
        db_model. Модель класса из базы данных.
    """
    def __init__(self, _class: models.page.Page) -> None:
        """Инициализация

        Args:
            _class - Модель класса из базы данных
        """
        super().__init__(_class.title)
        self.page = _class
