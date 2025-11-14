from db.models import page
from db import Session

from parsing.pyside6 import QFRFaqPage

from language import script as language_script


def safe_page_to_db(helper: QFRFaqPage) -> None:
    session = Session()

    func_description = ''
    for desc in helper.description:
        func_description += (language_script.translate(desc.text) + '\n\n')

    __page = page.Page(
        html_name=helper.html_name,
        title=helper.title,
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
            raw_args=func.name.raw_args
        )
        session.add(func)

    print('-- PROPERTY --')
    for _prop in helper.property:
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
