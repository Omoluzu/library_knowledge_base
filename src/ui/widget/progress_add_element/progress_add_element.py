from typing import Any

from .widget import ProgressAddElementWidget


class ProgressAddElement(ProgressAddElementWidget):
    """Прогресс добавления новых элементов"""
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация"""
        super().__init__(*args, **kwargs)

    def setTitle(self, title: str) -> None:
        """Установка заголовка

        Args:
            title (str): Заголовок
        """
        assert isinstance(title, str)
        self.name_upload_element.setText(title)

    def setTotalValue(self, total: int) -> None:
        """Установка максимального значение шагов для завершение загрузки

        Args:
            total (int): Устанавливаемое значение
        """
        assert isinstance(total, int)
        self.progress.setMaximum(total)
        self.progress.setValue(1)

    def increment(self) -> None:
        """Увеличение значение процесса выполнения на 1"""
        self.progress.setValue(self.progress.value() + 1)
