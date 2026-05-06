from typing import Optional, TYPE_CHECKING

import re


if TYPE_CHECKING:
    from bs4 import element


RE_MATH_TITLE = (
    r"(?:(?:\[(?P<type>.*)\])?"
    r"(?P<returns>.*[^(])?"
    r"(?:(?:\*?){title}(?:<\w>)?::)"
    r"(?P<name>\w*))(?:=)?"
    r"(?:\((?P<args>.*)\))?"
)


class PySide6FuncTitle:
    """Строка с наименование функции для PySide6"""
    def __init__(
            self, title_class_name: str, raw: "element.Tag"
    ) -> None:
        """Инициализация

        Args:
            title_class_name (str): Наименование заголовка класса
            raw (str): Неформатированный заголовок
        """
        self.title_class_name = title_class_name
        self.raw = raw

    def __str__(self) -> str:
        return self.name

    @property
    def _parse_title_func(self) -> re.Match[str]:
        """Получение данных при парсинге заголовка

        Returns:
            re.Match[str]: Данные заголовка
        """
        if not hasattr(self, "__cache_parse_title_func"):
            parse_title_func = re.match(
                RE_MATH_TITLE.format(title=self.title_class_name),
                self.raw.text)

            if parse_title_func:
                self.__cache_parse_title_func = parse_title_func

        return self.__cache_parse_title_func

    @property
    def raw_args(self) -> Optional[str]:
        """Получение неформатированных аргументов метода

        Returns:
            Неформатированный аргументы метода
        """
        try:
            return self._parse_title_func.group("args")
        except AttributeError:
            print("-->", self.title_class_name)
            raise AttributeError

    @property
    def raw_returns(self) -> str:
        """Получение неформатированных типов
        значений возвращаемых при вызове метода

        Returns:
            str: Неформатированный тип возвращаемых значений метода
        """
        return self._parse_title_func.group("returns")

    @property
    def name(self) -> str:
        """Получение наименование метода

        Returns:
            Имя метода
        """
        # NOTE. Старая реализация, удалить как подойдет время
        # return self._parse_title_func.group("name")

        name = self.raw["id"]
        assert isinstance(name, str)
        return name
