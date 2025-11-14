import os
import re

import requests
from bs4 import BeautifulSoup

URL = "https://registry.khronos.org/OpenGL-Refpages/gl4/html/{func_name}.xhtml"


class OpenGLFunc:
    """TODO:"""
    def __init__(self, func_name: str) -> None:
        """TODO: """
        self.name = func_name
        self.page = URL.format(func_name=self.name)

    @property
    def path_local_html_name(self) -> str:
        """TODO: """
        return os.path.join('html', 'opengl', f"{self.name}.html")

    @property
    def response(self):
        """TODO:"""
        return requests.get(self.page)

    @property
    def text(self) -> str:
        """Содержимое html страницы"""
        # Считываем данные из файла если файла создан.
        if os.path.exists(self.path_local_html_name):
            try:
                fd = os.open(self.path_local_html_name, flags=os.O_RDONLY)
                text = os.read(
                    fd, os.path.getsize(self.path_local_html_name)
                ).decode('utf-8')
            finally:
                os.close(fd)

            return text

        # Считывание данных с сайта и создание файла как буфера
        text = self.response.text
        while True:
            try:
                fd = os.open(
                    self.path_local_html_name, flags=os.O_WRONLY | os.O_CREAT)
                os.write(fd, text.encode('utf-8'))
            except FileNotFoundError:
                os.mkdir('html')
                os.mkdir('opengl')
                continue
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
    def description(self):
        """Получение описание текста"""
        desc = []

        div_description = self.soup.find('div', id='description')

        # TODO: Тут еще нужно будет выцепить <div class="variablelist">...</div>  # noqa
        for description in div_description.find_all(recursive=False):
            expr = re.sub(r"(\s{2,})", " ", description.text.replace('\n', ''))
            desc.append(expr)

        return desc
