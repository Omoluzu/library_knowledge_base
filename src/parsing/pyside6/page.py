import os
from typing import List

import requests
from bs4 import BeautifulSoup, element

from .page_func import QFRFaqPageFunc
from .page_property import QFRFaqPageProperty


# Qt for Russia (QFR)
class QFRFaqPage:
    def __init__(self, page_name: str):
        self.html_name = page_name
        self.page = f'https://doc.qt.io/qt-6/{self.html_name}.html'

    # @property
    # def html_name(self) -> str:
    #     return self.page.split('/')[-1][:-5]

    @property
    def path_local_html_name(self) -> str:
        return os.path.join('html', f"{self.html_name}.html")

    @property
    def response(self):
        return requests.get(self.page)

    @property
    def text(self) -> str:
        """Получение содержимое html страницы.
        Данные кэшируются в файл.
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
    def soup(self):
        return BeautifulSoup(self.text, 'html.parser')

    @property
    def content(self):
        return self.soup.find('div', class_='context')

    @property
    def title(self):
        return self.soup.find('h1', class_='title').text

    @property
    def requisites(self) -> element.Tag:
        """TODO: """
        return self.soup.find("table", class_="alignedsummary requisites")

    @property
    def func(self) -> List[QFRFaqPageFunc]:
        """Получения информации по функциями класса

        Returns:
            Список функций класса
        """
        fn = []

        for line in self.content.find('div', class_='func'):
            if isinstance(line, element.Tag):
                if line.attrs.get('class', [None])[0] == 'fn':
                    fn.append(QFRFaqPageFunc(parent=self, raw_name=line))
                else:
                    try:
                        fn[-1].append_description_raw(line)
                    except IndexError:
                        pass

        return fn

    @property
    def description(self) -> List[element.Tag]:
        """Получение исходного значение Описания класса

        Returns:
            Список абзацев описаний класса.
        """
        div_description = self.soup.find('div', class_='descr')
        return div_description.find_all('p')

    @property
    def prop(self) -> List[QFRFaqPageProperty]:
        """Получение информации по атрибутам класса

        Returns:
            Список атрибутов класса
        """
        prop = []

        try:
            for line in self.content.find('div', class_='prop'):
                if isinstance(line, element.Tag):
                    if line.attrs.get('class', [None])[0] == 'fn':
                        prop.append(QFRFaqPageProperty(
                            parent=self, raw_name=line))
                    else:
                        try:
                            prop[-1].append_description_raw(line)
                        except IndexError:
                            pass
        except TypeError:
            return []

        # print(prop)
        return prop

    @property
    def inherits(self) -> List[str]:
        """Наследуют

        Returns:
            List[str]: Список имен наследуемых классов
        """

        for tr in self.requisites.find_all("tr"):
            title, element = tr.find_all("td")
            if title.text == " Inherits:":
                return element.text.strip().split(' and ')

        return []

    @property
    def inherited_by(self) -> List[str]:
        """Унаследовано

        Returns:
            List[str]: Список классов унаследованных от текущего
        """
        return []
