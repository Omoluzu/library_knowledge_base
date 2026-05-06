from typing import List

from db import models, Session


class DBPageRepository:
    """Репозиторий страниц документации"""

    def __init__(self) -> None:
        """Инициализация, подключение к сессии базы данных"""
        self._session = Session()

    def get_all(self) -> List[models.page.Page]:
        """Запрос на получение всей информации из базы данных с
            наименование классов

        Returns:
            TODO:
        """
        return self._session.query(
            models.page.Page).order_by(models.page.Page.title).all()

    def get(self, name: str) -> models.page.Page:
        """Получение подели по её имени

        Args:
            name (str): наименование модели

        Returns:
            models.page.Page: models.page.Page
        """

        return self._session.query(
            models.page.Page).filter_by(title=name).one()

    def remove(self, models: models.page.Page) -> None:
        """TODO:

        Args:
            models (models.page.Page): _description_
        """
        for func in models.func:
            self._session.delete(func)

        self._session.delete(models)
        self._session.commit()
