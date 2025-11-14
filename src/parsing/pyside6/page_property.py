class QFRFaqPagePropertyTitle:
    def __init__(self, parent: object, raw: str) -> None:
        self.parent = parent
        self.raw = raw

    def __str__(self) -> str:
        return self.name

    @property
    def name(self) -> str:
        return self.raw.text.split(' : ')[0]


class QFRFaqPagePropertyDescription:
    def __init__(self, parent: object, raw: str) -> None:
        self.parent = parent
        self.raw = raw

    @property
    def text(self) -> str:
        return self.raw.text


class QFRFaqPageProperty:
    def __init__(self, parent: object, raw_name: str) -> None:
        """Инициализация

        Args:
            raw_name: HTML с наименованием атрибута
        """
        self.parent = parent
        self.name = QFRFaqPagePropertyTitle(parent=parent, raw=raw_name)
        self.description = []

    def append_description_raw(self, raw_description: str) -> None:
        """Добавление описания атрибута

        Args:
            raw_description: HTML абзац с описанием.
        """
        self.description.append(
            QFRFaqPagePropertyDescription(
                parent=self.parent, raw=raw_description))
