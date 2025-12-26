

### FIX QT
- QBoxLayout не правильно парсится метод инициализации. Из "QBoxLayout::QBoxLayout(QBoxLayout::Direction dir, QWidget *parent = nullptr)" я получаю "Direction(None) ->  QBoxLayout::QBoxLayout("


### QT
- QFRFaqPageFuncTitle документирование класса
- Скалить размер текста
- Возможность перейти на страницу сайта класса
- Определение типа методов.
- Определение атрибутов функции
- Отлов ошибок русификации текста (Сейчас они просто пропускаются, понять как с ними работать)
- Определение расположения классов (QtWidget, QtGui, QtCore)
- void QPushButton::setMenu(QMenu *menu)  - Ошибка вставки текста (Похоже что картинки) [setMenu](https://doc.qt.io/qt-6/qpushbutton.html#setMenu)
- void QAbstractButton::toggled(bool checked)  - Ошибка при попытки локализовать код [toggled](https://doc.qt.io/qt-6/qabstractbutton.html#toggled)

### OpenGL
- Добавить библиотеку PyOpenGL.
- В Description получить значения для <div class="variablelist">...</div> 

### OTHER
- Добавить весь синтаксис Python и всех PEP.
- Реализовать все библиотеки с которыми мне приходится работать.
- Может быть даже добавить все системные вызовы.
