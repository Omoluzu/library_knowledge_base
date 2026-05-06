import sys
import asyncio
from typing import Any


from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
)

from qasync import QEventLoop

from ui import widget


class MainFQRFaqWindow(QMainWindow):
    """Головной виджет"""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация"""
        super().__init__(*args, **kwargs)
        self.resize(1300, 600)

        self.setWindowTitle('База знаний библиотек')  # Library knowledge base
        self.main_widget = widget.MainCentral()
        self.setCentralWidget(self.main_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    window = MainFQRFaqWindow()
    window.show()

    with loop:
        loop.run_forever()
