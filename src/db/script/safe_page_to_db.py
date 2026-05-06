import time
import traceback
from typing import List, Any

from db import Session
from db.models import page
from parsing.pyside6 import QFRFaqPage
from PySide6.QtCore import Signal, QThread, QObject
from language import script as language_script


class TranslateObject(QThread):
    """TODO:"""
    message = Signal(dict)
    """TODO:"""
    error = Signal(str)
    """TODO: """

    def __init__(
            self, parent: QObject, name: str, *args: Any, **kwargs: Any
    ) -> None:
        """TODO: """
        super().__init__(parent, *args, **kwargs)
        self.name = name

    def run(self) -> None:
        """TODO:"""
        try:
            helper = QFRFaqPage(page_name=self.name)
            try:
                self.message.emit({
                    "command": "start_translate", "title": helper.title(),
                    "total": len(helper.func) + len(helper.prop),
                })
            except AttributeError:
                print(f"run.AttributeError.name = {self.name}")
                raise

            session = Session()

            func_description = ''
            for desc in helper.description:
                func_description += (
                    language_script.translate(desc.text) + '\n\n')

            __page = page.Page(
                html_name=helper.html_name,
                title=helper.title(),
                inherits=",".join(helper.inherits),
                description_ru=func_description,
            )
            session.add(__page)
            session.commit()

            for helper_func in helper.func:
                list_desc: List[str] = []
                for description in helper_func.description:
                    list_desc.append(
                        language_script.translate(description.text))
                    time.sleep(.05)

                self.message.emit({
                    "command": "add_translate",  "type": "func",
                    "translate": helper_func.name.name, "title": helper.title()
                })
                save_desc = '\n'.join(list_desc)
                func = page.PageFunc(
                    name=str(helper_func.name),
                    page=__page,
                    description_ru=save_desc,
                    raw_args=helper_func.name.raw_args,
                    raw_returns=helper_func.name.raw_returns,
                )
                session.add(func)

            for _prop in helper.prop:
                list_prop: List[str] = []
                for _description in _prop.description:
                    list_prop.append(
                        language_script.translate(_description.text))
                    time.sleep(.05)

                self.message.emit({
                    "command": "add_translate", "translate": _prop.name.name,
                    "type": "property", "title": helper.title()
                })
                save_prop = '\n'.join(list_prop)
                prop = page.PageFunc(
                    name=str(_prop.name),
                    page=__page,
                    description_ru=save_prop
                )
                session.add(prop)

            session.commit()

            self.message.emit({
                "command": "finished_translate",
                "title": helper.title()
            })

        except Exception:
            self.error.emit(traceback.format_exc)
            traceback.print_exc()

        finally:
            self.deleteLater()


def safe_page_to_db(helper: QFRFaqPage) -> None:
    session = Session()

    func_description = ''
    for desc in helper.description:
        func_description += (language_script.translate(desc.text) + '\n\n')

    __page = page.Page(
        html_name=helper.html_name,
        title=helper.title(),
        inherits=",".join(helper.inherits),
        description_ru=func_description,
    )
    session.add(__page)
    session.commit()

    print('-- FUNCTION --')
    for func in helper.func:
        list_desc: List[str] = []
        for func_desc in func.description:
            list_desc.append(language_script.translate(func_desc.text))

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
        list_prop: List[str] = []
        for prop_desc in _prop.description:
            list_prop.append(language_script.translate(prop_desc.text))

        print(_prop.name)
        save_prop = '\n'.join(list_prop)
        prop = page.PageFunc(
            name=str(_prop.name),
            page=__page,
            description_ru=save_prop
        )
        session.add(prop)

    session.commit()
