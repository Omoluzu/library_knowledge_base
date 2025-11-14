from sqlalchemy import create_engine

from .config import MAIN_DB_URL, OPENGL_DB_URL

main_engine = create_engine(MAIN_DB_URL)
opengl_engine = create_engine(OPENGL_DB_URL)
