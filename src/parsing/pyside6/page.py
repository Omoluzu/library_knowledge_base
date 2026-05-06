import os
from typing import List, Union, Optional, Iterator

import requests
from bs4 import BeautifulSoup, element

from .title import PySide6Title
from .page_func import PySide6WidgetFunc
from .property import PySide6Property


# Qt for Russia (QFR)
class QFRFaqPage:
    """TODO: """
    def __init__(self, page_name: str) -> None:
        self.html_name = page_name
        self.page = rf"https://doc.qt.io/qt-6/{self.html_name}.html"

    @property
    def path_local_html_name(self) -> str:
        """TODO: """
        return os.path.join("html", f"{self.html_name}.html")

    @property
    def response(self):
        """TODO: """
        return requests.get(self.page)

    @property
    def text(self) -> str:
        """Получение содержимое html страницы.
        Данные кэшируются в файл.

        Returns:
            TODO:
        """
        if os.path.exists(self.path_local_html_name):
            try:
                fd = os.open(self.path_local_html_name, flags=os.O_RDONLY)
                text = os.read(
                    fd, os.path.getsize(self.path_local_html_name)
                ).decode('utf-8')
            except Exception as e:
                raise e
            finally:
                os.close(fd)

            return text

        text = self.response.text

        while True:
            try:
                fd = os.open(
                    self.path_local_html_name, flags=os.O_WRONLY | os.O_CREAT)
                os.write(fd, text.encode('utf-8'))
            except FileNotFoundError:
                os.mkdir('html')
                continue
            except Exception as e:
                raise e
            else:
                break
            finally:
                try:
                    os.close(fd)
                except UnboundLocalError:
                    pass

        return text

    @property
    def soup(self) -> BeautifulSoup:
        """TODO:

        Returns:
            _type_: _description_
        """
        return BeautifulSoup(self.text, 'html.parser')

    @property
    def context(self) -> Optional[
            Union[element.PageElement, element.Tag, element.NavigableString]]:
        """TODO:

        Returns:
            _type_: _description_
        """
        return self.soup.find('div', class_='context')

    @property
    def title(self) -> PySide6Title:
        """Получение заголовка класса

        Returns:
            str: Заголовок класса
        """
        raw_title = self.soup.find('h1', class_='title')
        assert isinstance(raw_title, element.Tag)
        return PySide6Title(raw=raw_title)

    @property
    def requisites(self) -> element.Tag:
        """TODO:

        Returns:
            element.Tag: _description_
        """
        table = self.soup.find("table", class_="alignedsummary requisites")
        assert isinstance(table, element.Tag)
        return table

    @property
    def func(self) -> List[PySide6WidgetFunc]:
        """Получения информации по функциями класса

        Returns:
            Список функций класса
        """
        fn: List[PySide6WidgetFunc] = []

        div = self.context.find('div', class_='func')
        assert isinstance(div, element.Tag)
        for line in div:
            if isinstance(line, element.Tag):
                if line.attrs.get('class', [None])[0] == 'fn':
                    fn.append(PySide6WidgetFunc(parent=self, raw_name=line))
                else:
                    try:
                        fn[-1].append_description_raw(line)
                    except IndexError:
                        pass

        return fn

    @property
    def description(self) -> Iterator[element.Tag]:
        """Получение исходного значение Описания класса

        Returns:
            Список абзацев описаний класса.
        """
        div_description = self.soup.find('div', class_='descr')
        assert isinstance(div_description, element.Tag)
        for tag_p in div_description.find_all('p'):
            assert isinstance(tag_p, element.Tag)
            yield tag_p

    @property
    def prop(self) -> List[PySide6Property]:
        """Получение информации по атрибутам класса

        Returns:
            Список атрибутов класса
        """
        prop: List[PySide6Property] = []

        try:
            for line in self.context.find('div', class_='prop'):
                if isinstance(line, element.Tag):
                    if line.attrs.get('class', [None])[0] == 'fn':
                        prop.append(PySide6Property(raw_name=line))
                    else:
                        try:
                            prop[-1].append_description_raw(line)
                        except IndexError:
                            pass
        except TypeError:
            return []

        return prop

    @property
    def inherits(self) -> List[str]:
        """Получение объектов от которых наследуется текущий объект

        Returns:
            List[str]: Список имен наследуемых классов
        """

        for tr in self.requisites.find_all("tr"):
            title, _element = tr.find_all("td")

            if (
                    isinstance(title, element.Tag)
                    and title.text == " Inherits:"
                    and isinstance(_element, element.Tag)
            ):
                return _element.text.strip().split(" and ")

        return []

    @property
    def inherited_by(self) -> List[str]:
        """Унаследовано

        Returns:
            List[str]: Список классов унаследованных от текущего
        """
        return []
