from typing import Optional

import re

RE_MATH_TITLE = (
    r"(?:(?:(?P<return_type>\[.*\])(?: ))?)"
    r"(const )?"
    r"(\w* ?<.*> )?"
    r"((?:\w*::)\w* ?)?(\w* )?"
    r"(?:(?P<class>(?:\&?)(?:\*?){title}(?:<\w>)?::)"
    r"(?P<name>\w*))"
    r"(?:=)?"
    r"(?:\((?P<args>.*)\))?"
)


class PySide6FuncTitle:
    """Строка с наименование функции для PySide6"""
    def __init__(self, parent: object, raw: str) -> None:
        """Инициализация

        Args:
            parent (object): Родитель
            raw (str): Неформатированный заголовок
        """
        self.parent = parent
        self.raw = raw

    def __str__(self) -> str:
        return self.name

    @property
    def title(self) -> str:
        """Получение заголовка метода"""
        title: str = self.parent.title.strip()  # TODO: Фу. Parent

        if 'Class' in title:
            title = title.removesuffix('Class').strip()

        return title

    @property
    def _parse_title_func(self) -> re.Match[str]:
        """Парсинг заголовка"""
        if not hasattr(self, '__cache_parse_title_func'):
            self.__cache_parse_title_func = re.match(
                RE_MATH_TITLE.format(title=self.title),
                self.raw.text)

        return self.__cache_parse_title_func

    @property
    def raw_args(self) -> Optional[str]:
        """Получение неформатированныхх аргументов метода

        Returns:
            Неформатированный аргументы метода
        """
        try:
            return self._parse_title_func.group('args')
        except AttributeError:
            print("-->", self.title)
            raise AttributeError

    @property
    def name(self) -> str:
        """Получение наименование метода

        Returns:
            Имя метода
        """
        return self._parse_title_func.group('name')
