from typing import Any, Dict, TYPE_CHECKING

from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt
from db import script

from .widget import MainCentralWidget


if TYPE_CHECKING:
    from ui.widget import ProgressAddElement


class MainCentral(MainCentralWidget):
    """Центральный основной виджет"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация"""
        super().__init__(*args, **kwargs)

        self.progress_elements: Dict[str, "ProgressAddElement"] = {}

        # ----- CONFIG
        self.add_element_popup.hide()

        # ----- CONNECT
        self.add_element_popup.addElement.connect(self.slot_add_element)
        self.add_element_button.clicked.connect(
            self.slot_show_add_element_dialog)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if (
                event.modifiers() == Qt.KeyboardModifier.ControlModifier
                and event.key() == Qt.Key.Key_N
        ):
            self.slot_show_add_element_dialog()

        super().keyPressEvent(event)

    def slot_show_add_element_dialog(self) -> None:
        """Вызов диалогового окна на добавление нового элемента"""
        self.add_element_popup.show()
        self.add_element_popup.raise_()

    def slot_add_element(self, name: str) -> None:
        """Добавление нового элемента"""
        save = script.TranslateObject(self, name)
        save.message.connect(self.slot_save_message)
        save.error.connect(self.slot_save_error)
        save.start()

    def slot_save_error(self, error: str) -> None:
        print(f"[ERROR]: {error}")

    def slot_save_message(self, message: Dict[str, Any]) -> None:
        """Слот получения сообщения от функции перевода строк

        Args:
            message (Dict[str, Any]): Входящее сообщение
        """
        from ui import widget
        print("--->", message)

        match message["command"]:
            case "start_translate":
                self.add_element_popup.hide()

                title: str = message["title"]

                self.progress_elements[title] = widget.ProgressAddElement()
                self.progress_elements[title].setParent(self)
                self.progress_elements[title].show()
                self.progress_elements[title].setTitle(message["title"])
                self.progress_elements[title].setTotalValue(message["total"])

                count = len(self.progress_elements)
                self.progress_elements[title].move(
                    self.width() - self.progress_elements[title].width() - 10,
                    (
                        self.height() - (
                            (self.progress_elements[title].height() + 5)
                            * count) - 15
                    )
                )

            case "add_translate":
                self.progress_elements[message["title"]].increment()

            case "finished_translate":
                title: str = message["title"]
                self.progress_elements[title].setParent(None)
                self.progress_elements[title].deleteLater
                del self.progress_elements[title]

                self.pyside6_widget.refresh_pages()

                # Обновляем позиции виджетов
                for i, progress_element in enumerate(
                        self.progress_elements.values(), start=1
                ):

                    progress_element.move(
                        self.width() - progress_element.width() - 10,
                        (
                            self.height()
                            - ((progress_element.height() + 5) * i) - 15
                        )
                    )

            case _:
                print("Unsupported message command", message)
