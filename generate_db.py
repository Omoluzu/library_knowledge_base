from parsing import pyside6, opengl
from db import script as db_script
from db import Session
from db.models.opengl import OpenGlFunc
from language import script as language_script

list_page_qt = [
    "qfuture",
    "qrawfont",
    "qlistwidgetitem",
    "qlistwidget",
    "qstatemachine",
    "qwebengineview",
    "qlineedit",
    "qbuttongroup",
    "qtabwidget",
    "qstackedwidget",
    "qstackedlayout",
    "qboxlayout",
    "qlabel",
    "qlayout",
    "qtextedit",
    "qpushbutton",
    "qabstractbutton",
    "qwidget",
    "qrect",
    "qregularexpression",
    "qfontmetrics",
    "qcombobox",
    "qfocusevent",
    "qprogressbar",
    "qscrollbar",
    "qobject",
    "qcheckbox",
    "qscrollarea",
    "qabstractscrollarea",
    "qframe",
    "qrunnable",
    "qtextcursor",
    "qtextblock",
    "qtextdocument"
]

list_page_opengl = [
    'glStencilOp'
]


if __name__ == '__main__':

    db_script.create_tables()

    helper = pyside6.QFRFaqPage(page_name='qtextdocument')
    db_script.safe_page_to_db(helper=helper)

    # for page in list_page:
    #     helper = QFRFaqPage(page_name=page)
    #     db_script.safe_page_to_db(helper=helper)

    # gl = opengl.OpenGLFunc(func_name='glStencilOp')

    # session = Session()

    # list_desc = []
    # for desc in gl.description:
    #     list_desc.append(language_script.translate(desc))

    # save_desc = '\n'.join(list_desc)
    # # opengl.OpenGlFunc(
    # #     name='glStencilOp',
    # #     description_ru=save_desc
    # # )
    # session.add(OpenGlFunc(
    #     name='glStencilOp',
    #     description_ru=save_desc
    # ))

    # session.commit()
