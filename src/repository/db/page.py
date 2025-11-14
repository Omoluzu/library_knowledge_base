from typing import List

from db import models, Session


class DBPageRepository:
    """Репозиторий страниц документации"""
    def __init__(self):
        """Инициализация, подключение к сессии базы данных"""
        self._session = Session()

    def get_all(self) -> List[models.page.Page]:
        """Запрос на получение всей информации из базы данных с
            наименование классов"""
        return self._session.query(
            models.page.Page).order_by(models.page.Page.title).all()
