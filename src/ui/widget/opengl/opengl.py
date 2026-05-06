from typing import Any


from PySide6.QtWidgets import (
    QWidget,
    QTextEdit,
    QSplitter,
    QListWidget,
    QHBoxLayout,
    QListWidgetItem,
)


from repository import db


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
