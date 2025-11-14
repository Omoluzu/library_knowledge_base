from typing import List

from db import models, Session


class DBOpenGLRepository:
    """Репозиторий страниц документации"""
    def __init__(self):
        """Инициализация, подключение к сессии базы данных"""
        self._session = Session()

    def get_all(self) -> List[models.opengl.OpenGlFunc]:
        """Запрос на получение всей информации из базы данных с
            наименование классов"""
        return self._session.query(
            models.opengl.OpenGlFunc
        ).order_by(models.opengl.OpenGlFunc.name).all()

    def get_by_name(self, name: str) -> models.opengl.OpenGlFunc:
        """TODO:"""
        return self._session.query(
            models.opengl.OpenGlFunc).filter_by(name=name).one()
