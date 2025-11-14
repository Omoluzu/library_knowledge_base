import sys
import asyncio


from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QHBoxLayout,
    QTextEdit,
    QSplitter,
    QTabWidget,
    QListWidget,
    QListWidgetItem,
)
from qasync import QEventLoop

from db import models
from ui import widget
from repository import db


class PySide6Widget(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._repo_page = db.DBPageRepository()

        _pages_widget = widget.NameClassWidget()
        self.func_widget = widget.func.NameFuncWidget()
        self.description_widget = QTextEdit()

        _pages_widget.addItem(self._repo_page.get_all())

        _pages_widget.itemClicked.connect(self.slot_item_clicked)
        self.func_widget.itemClicked.connect(self.slot_func_item_clicked)

        main_splitter = QSplitter()
        main_splitter.addWidget(_pages_widget)
        main_splitter.addWidget(self.func_widget)
        main_splitter.addWidget(self.description_widget)

        main_layout = QHBoxLayout()
        main_layout.addWidget(main_splitter)
        self.setLayout(main_layout)

    def slot_item_clicked(self, item: models.page.Page) -> None:
        """Клик по наименованию виджет"""
        self.func_widget.addItem(item.func)
        self.description_widget.setText(item.description_ru)

    def slot_func_item_clicked(
            self, item: models.page.PageFunc) -> None:
        """Клик по наименование метода"""
        self.description_widget.clear()

        text = f"{item.name}({item.raw_args})\n\n{item.description_ru}"
        self.description_widget.setText(text)


class OpenGLWidget(QWidget):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._repo_opengl = db.DBOpenGLRepository()

        opengl_list_func_widget = QListWidget()
        for opengl_model in self._repo_opengl.get_all():
            opengl_list_func_widget.addItem(QListWidgetItem(opengl_model.name))
        opengl_list_func_widget.itemClicked.connect(
            self.slot_load_description_opengl)

        self.opengl_text_edit = QTextEdit()

        main_splitter = QSplitter()
        main_splitter.addWidget(opengl_list_func_widget)
        main_splitter.addWidget(self.opengl_text_edit)

        main_layout = QHBoxLayout()
        main_layout.addWidget(main_splitter)
        self.setLayout(main_layout)

    def slot_load_description_opengl(self, item: QListWidgetItem) -> None:
        """Загрузка описания выбранной функции OpenGL"""
        opengl_model = self._repo_opengl.get_by_name(name=item.text())
        self.opengl_text_edit.setPlainText(opengl_model.description_ru)


class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.tabs = QTabWidget()

        self.tabs.addTab(PySide6Widget(), "PySide6")
        self.tabs.addTab(OpenGLWidget(), "OpenGL")

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)


class MainFQRFaqWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('База знаний библиотек')  # Library knowledge base
        self.main_widget = CentralWidget()
        self.setCentralWidget(self.main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = MainFQRFaqWindow()
    window.show()

    with loop:
        loop.run_forever()
