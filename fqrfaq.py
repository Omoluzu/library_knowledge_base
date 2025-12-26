import sys
import asyncio
from typing import Any, Optional


from PySide6.QtWidgets import (
    QWidget,
    QTextEdit,
    QSplitter,
    QTabWidget,
    QListWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMainWindow,
    QApplication,
    QListWidgetItem,
)
from PySide6.QtCore import QSize, Qt, QThreadPool

from qasync import QEventLoop  # type: ignore

from db import script
from repository import db
from parsing import pyside6
from ui import widget, popup


class OpenGLWidget(QWidget):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._repo_opengl = db.DBOpenGLRepository()

        opengl_list_func_widget = QListWidget()
        for opengl_model in self._repo_opengl.get_all():
            opengl_list_func_widget.addItem(
                QListWidgetItem(str(opengl_model.name)))
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
        self.opengl_text_edit.setPlainText(str(opengl_model.description_ru))


class CentralWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.thread_pool: QThreadPool = QThreadPool.globalInstance()

        self.pyside6_widget = widget.PySide6Widget()

        # self.save_object = script.SafeObject()

        self.add_element_popup: Optional[popup.AddElementPopup] = None
        self.add_element_button = QPushButton('+')

        self.setConfig()
        self.setupUI()

    def slot_show_add_element_dialog(self) -> None:
        """Вызов диалогового окна на добавление нового элемента"""
        self.add_element_popup = popup.AddElementPopup(self)
        self.add_element_popup.addElement.connect(self.slot_add_element)
        self.add_element_popup.show()

    def slot_add_element(self, name: str) -> None:
        """Добавление нового элемента"""

        safe = script.SafeRunnable(name)
        safe.signals.finished.connect(self.slot_save_finished)

        self.thread_pool.start(safe)

        # helper = pyside6.QFRFaqPage(page_name=name)
        # asyncio.create_task(self.save_object.run(helper))

    def slot_save_finished(self) -> None:
        """TODO:
        """
        if isinstance(self.add_element_popup, popup.AddElementPopup):
            self.add_element_popup.setParent(None)

        self.pyside6_widget.refresh_pages()

    def setConfig(self) -> None:
        """Конфигурация"""
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)

        self.add_element_button.setFixedSize(QSize(40, 40))
        self.add_element_button.clicked.connect(
            self.slot_show_add_element_dialog)

        # self.save_object.finished.connect(self.slot_save_finished)

    def setupUI(self) -> None:
        """UI"""
        tabs = QTabWidget()
        tabs.addTab(self.pyside6_widget, "PySide6")
        tabs.addTab(OpenGLWidget(), "OpenGL")

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.add_element_button)
        main_layout.addWidget(tabs)
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
