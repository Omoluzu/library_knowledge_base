
### FIX APP
- Если в базе данных уже есть запись а мы её пытаемся добавить то выходит ошибка. Лучше перейти на реализацию виджета


### FIX QT
- QStyleOption https://doc.qt.io/qt-6/qstyleoption.html#rect-var не видит все "Public Variables"
- Не могу распарсить следующую страницу https://doc.qt.io/qt-6/qtextedit-extraselection.html при указании qtextedit-extraselection в поиск
- Плохо парсит методы QRegularExpression 

### QT
- Скалить размер текста
- Возможность перейти на страницу сайта класса
- Определение типа методов.
- Отлов ошибок русификации текста (Сейчас они просто пропускаются, понять как с ними работать)
- Определение расположения классов (QtWidget, QtGui, QtCore)
- void QPushButton::setMenu(QMenu *menu)  - Ошибка вставки текста (Похоже что картинки) [setMenu](https://doc.qt.io/qt-6/qpushbutton.html#setMenu)
- void QAbstractButton::toggled(bool checked)  - Ошибка при попытки локализовать код [toggled](https://doc.qt.io/qt-6/qabstractbutton.html#toggled)
- Обновление данных класса из приложения (ПКМ -> обновить -> загрузить новую html с сайта и расспарсить заново)
- Поиск по названием класса.
- При создании нового класса если класс уже есть либо перейти на него либо перекачать

### OpenGL
- Добавить библиотеку PyOpenGL.
- В Description получить значения для <div class="variablelist">...</div> 

### OTHER
- Добавить весь синтаксис Python и всех PEP.
- Реализовать все библиотеки с которыми мне приходится работать.
- Может быть даже добавить все системные вызовы.
