from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


OpenGLBase = declarative_base()


class OpenGlFunc(OpenGLBase):
    __tablename__ = 'opengl_func'
    __bind_key__ = 'opengl'

    id = Column(Integer, primary_key=True)

    name = Column(String)

    # parameters_ru = Column(String)

    description_ru = Column(String)
