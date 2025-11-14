from .connection import main_engine, opengl_engine
from .models.page import QtBase
from .models.opengl import OpenGLBase


from sqlalchemy.orm import sessionmaker


# Session = sessionmaker(bind=main_engine)

# Session = sessionmaker(binds={
#     QtBase: main_engine,
#     OpenGLBase: opengl_engine
# })


class Session:
    _instance = None
    __session = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Session, cls).__new__(cls)
            cls.__session = sessionmaker(binds={
                QtBase: main_engine,
                OpenGLBase: opengl_engine
            })()

        return cls._instance

    def __getattr__(self, name):
        return getattr(self.__session, name)
