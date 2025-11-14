from db.models import page, opengl
from db.connection import main_engine, opengl_engine


def create_tables():
    page.QtBase.metadata.create_all(main_engine)
    opengl.OpenGLBase.metadata.create_all(opengl_engine)
