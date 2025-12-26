from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


QtBase = declarative_base()


class Page(QtBase):
    __tablename__ = 'pages'
    __bind_key__ = 'qt'

    id = Column(Integer, primary_key=True)

    html_name = Column(String, unique=True, nullable=False)

    title = Column(String, unique=True, nullable=False)

    inherits = Column(String, default=None, nullable=True)

    description_ru = Column(String)

    func = relationship('PageFunc', backref=backref('page', lazy='joined'))


class PageFunc(QtBase):
    __tablename__ = 'pages_func'
    __bind_key__ = 'qt'

    id = Column(Integer, primary_key=True)

    name = Column(String)

    page_id = Column(Integer, ForeignKey('pages.id'))

    description_ru = Column(String)

    raw_args = Column(String, nullable=True)

    raw_returns = Column(String, nullable=True)
