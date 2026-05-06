from typing import Any

from PySide6.QtWidgets import QListWidgetItem

from db import models


class TitleClassItemWidget(QListWidgetItem):
    """Отдельный элемент списка наименований классов."""

    def __init__(
            self, page_model: models.page.Page, *args: Any, **kwargs: Any
    ) -> None:
        """Инициализация

        Args:
            page_model (models.page.Page): Модель класса из базы данных
        """
        super().__init__()

        self.model_page: models.Page = page_model
        """Модель класса из базы данных"""

        self.setConfig()

    def setConfig(self) -> None:
        self.setText(str(self.model_page.title))
