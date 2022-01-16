class Reader:

    def __init__(self, name: str, surname: str, years: int,
                 id_=None) -> None:
        self.__name = name
        self.__surname = surname
        self.__years = years

        self.__id = id_ if id_ else id(self)

    def get_name(self) -> str:
        """
         Method return name
        :param
        :return: str
        """
        return self.__name

    def get_surname(self) -> str:
        """
         Method return surname
        :param
        :return: str
        """
        return self.__surname

    def get_years(self) -> int:
        """
         Method return years
        :param
        :return: int
        """
        return self.__years

    def get_id(self) -> int:
        """
         Method return id
        :param
        :return: int
        """
        return self.__id

    def dict(self) -> dict:
        cls_name = __class__.__name__
        return {
            attr.replace(f'_{cls_name}__', ''): getattr(self, attr)
            for attr in dir(self) if attr.startswith(f'_{cls_name}__')
        }

    @classmethod
    def from_dict(cls, _dict_book: dict):
        return cls(
            name=_dict_book['name'],
            surname=_dict_book['surname'],
            years=_dict_book['years'],
            id_=_dict_book['id'],
        )

    def __str__(self):
        return f'{self.__id}) {self.__name} {self.__surname}, {self.__years}.'

    def __repr__(self):
        cls_name = __class__.__name__
        return ''.join(
            [
                f'{attr.replace(f"_{cls_name}__", "")}={getattr(self, attr)} '
                for attr in dir(self) if attr.startswith(f'_{cls_name}__')
            ]
        )