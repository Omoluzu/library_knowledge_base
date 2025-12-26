import asyncio
from multiprocessing import Pool

from PySide6.QtCore import QObject, Signal, QRunnable

from db import Session
from db.models import page
# from parsing import pyside6
from parsing.pyside6 import QFRFaqPage
from language import script as language_script


class SafeRunnable(QRunnable):
    class Signals(QObject):
        # Сигнал завершения процесса просчета точек для отрисовки заготовок
        finished = Signal()
        # Сигнал передающий исключение возникшее в процессе работы.
        error = Signal(str)

    def __init__(self, name: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name = name
        self.signals = self.Signals()

    def run(self) -> None:
        try:
            with Pool(processes=1) as pool:
                pool.apply(self.run_save_object, (self.name,))
                self.signals.finished.emit()

        except Exception as e:
            print("Exception", str(e))
            self.signals.error.emit(str(e))

    @staticmethod
    def run_save_object(name: str) -> None:
        helper = QFRFaqPage(page_name=name)

        session = Session()

        func_description = ''
        for desc in helper.description:
            func_description += (language_script.translate(desc.text) + '\n\n')

        __page = page.Page(
            html_name=helper.html_name,
            title=helper.title,
            inherits=",".join(helper.inherits),
            description_ru=func_description,
        )
        session.add(__page)
        session.commit()

        print('-- FUNCTION --')
        for func in helper.func:
            list_desc = []
            for desc in func.description:
                list_desc.append(language_script.translate(desc.text))

            print(func.name)
            save_desc = '\n'.join(list_desc)
            func = page.PageFunc(
                name=str(func.name),
                page=__page,
                description_ru=save_desc,
                raw_args=func.name.raw_args,
                raw_returns=func.name.raw_returns,
            )
            session.add(func)

        print('-- PROPERTY --')
        for _prop in helper.prop:
            list_prop = []
            for desc in _prop.description:
                list_prop.append(language_script.translate(desc.text))

            print(_prop.name)
            save_prop = '\n'.join(list_prop)
            prop = page.PageFunc(
                name=str(_prop.name),
                page=__page,
                description_ru=save_prop
            )
            session.add(prop)

        session.commit()


class SafeObject(QObject):
    finished = Signal()

    async def run(self, helper: QFRFaqPage) -> None:
        session = Session()

        func_description = ''
        for desc in helper.description:
            text = await language_script.async_translate(desc.text)
            func_description += (text + '\n\n')

        __page = page.Page(
            html_name=helper.html_name,
            title=helper.title,
            inherits=",".join(helper.inherits),
            description_ru=func_description,
        )
        session.add(__page)
        session.commit()

        print('-- FUNCTION --')
        for func in helper.func:
            list_desc = []
            for desc in func.description:
                text = await language_script.async_translate(desc.text)
                list_desc.append(text)
                # await asyncio.sleep(.1)

            print(func.name)
            save_desc = '\n'.join(list_desc)
            func = page.PageFunc(
                name=str(func.name),
                page=__page,
                description_ru=save_desc,
                raw_args=func.name.raw_args,
                raw_returns=func.name.raw_returns,
            )
            session.add(func)

        print('-- PROPERTY --')
        for _prop in helper.prop:
            list_prop = []
            for desc in _prop.description:
                text = await language_script.async_translate(desc.text)
                list_prop.append(text)
                # await asyncio.sleep(.1)

            print(_prop.name)
            save_prop = '\n'.join(list_prop)
            prop = page.PageFunc(
                name=str(_prop.name),
                page=__page,
                description_ru=save_prop
            )
            session.add(prop)

        session.commit()

        self.finished.emit()


def safe_page_to_db(helper: QFRFaqPage) -> None:
    session = Session()

    func_description = ''
    for desc in helper.description:
        func_description += (language_script.translate(desc.text) + '\n\n')

    __page = page.Page(
        html_name=helper.html_name,
        title=helper.title,
        inherits=",".join(helper.inherits),
        description_ru=func_description,
    )
    session.add(__page)
    session.commit()

    print('-- FUNCTION --')
    for func in helper.func:
        list_desc = []
        for desc in func.description:
            list_desc.append(language_script.translate(desc.text))

        print(func.name)
        save_desc = '\n'.join(list_desc)
        func = page.PageFunc(
            name=str(func.name),
            page=__page,
            description_ru=save_desc,
            raw_args=func.name.raw_args,
            raw_returns=func.name.raw_returns,
        )
        session.add(func)

    print('-- PROPERTY --')
    for _prop in helper.prop:
        list_prop = []
        for desc in _prop.description:
            list_prop.append(language_script.translate(desc.text))

        print(_prop.name)
        save_prop = '\n'.join(list_prop)
        prop = page.PageFunc(
            name=str(_prop.name),
            page=__page,
            description_ru=save_prop
        )
        session.add(prop)

    session.commit()
