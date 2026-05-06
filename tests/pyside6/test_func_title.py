import pytest
from bs4 import BeautifulSoup

from parsing.pyside6.page_func_title import PySide6FuncTitle


title_get_color = """<h3 class="fn" id="getColor" translate="no">
<code class="details extra" translate="no">[static]</code>
<span class="type">
    <a href="qcolor.html" translate="no">QColor</a>
</span>
    QColorDialog::
<span class="name">getColor</span>(const <span class="type">
    <a href="qcolor.html" translate="no">QColor</a></span> &amp;<i>initial</i> = Qt::white, <span class="type"><a href="qwidget.html" translate="no">QWidget</a></span> *<i>parent</i> = nullptr, const <span class="type"><a href="qstring.html" translate="no">QString</a></span> &amp;<i>title</i> = QString(), <span class="type"><a href="qcolordialog.html#ColorDialogOption-enum" translate="no">QColorDialog::ColorDialogOptions</a></span> <i>options</i> = ColorDialogOptions())<a class="srclink" href="https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/dialogs/qcolordialog.h?h=6.11#n56" title="View declaration of this function"></a><a class="plink" href="#getColor" title="Direct link to this headline"></a></h3>"""  # noqa
title_done = """<h3 class="fn" id="done" translate="no">
<code class="details extra" translate="no">[override virtual protected]</code>
<span class="type">void</span>
    QColorDialog::
<span class="name">done</span>(<span class="type">int</span> <i>result</i>)
    <a class="srclink" href="https://code.qt.io/cgit/qt/qtbase.git/tree/src/widgets/dialogs/qcolordialog.h?h=6.11#n73" title="View declaration of this function"></a><a class="plink" href="#done" title="Direct link to this headline"></a></h3>"""  # noqa


@pytest.mark.parametrize("title_class,result,parser", [
    ("QColorDialog", "done", title_done),
    ("QColorDialog", "getColor", title_get_color),
])
def test_title(title_class: str, result: str, parser: str) -> None:
    """Тестирование получение заголовочной информации

    Args:
        title_class (str): TODO:
        result (str): TODO:
        parser (str): TODO:
    """
    h3_tag = BeautifulSoup(parser, features="html.parser").h3
    assert h3_tag is not None

    done = PySide6FuncTitle(title_class_name=title_class, raw=h3_tag)
    assert done.name == result
