from typing import Union


class Book:
    """Class which describe book"""

    def __init__(self, title: str, author: str, years: int,
                 id_=None, reader_id=None) -> None:
        self.__title = title
        self.__author = author
        self.__years = years

        self.__id = id_ if id_ else id(self)
        self.__reader_id = reader_id

    def get_title(self) -> str:
        """
         Method return title
        :param
        :return: str
        """
        return self.__title

    def get_author(self) -> str:
        """
           Method return author
          :param
          :return: str
          """
        return self.__author

    def get_years(self) -> int:
        """
         Method return year
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

    def get_reader_id(self) -> int:
        """
         Method return reader_id
        :param
        :return: int
        """
        return self.__reader_id

    def set_reader_id(self, _reader_id: Union[int, None]) -> None:
        """
         Method set reader_id
        :param
        :return: bool
        """
        self.__reader_id = _reader_id

    def dict(self) -> dict:
        return {
            'title':self.__title,
            'author': self.__author,
            'years': self.__years,
            'id_': self.__id,
            'reader_id': self.__reader_id,
        }

        # cls_name = __class__.__name__
        # # _Book__title
        # return {
        #     attr.replace(f'_{cls_name}__', ''): getattr(self, attr)
        #     for attr in dir(self) if attr.startswith(f'_{cls_name}__')
        # }

    @classmethod
    def from_dict(cls, _dict_book: dict):
        """
        returns a new dictionary with the passed memories as keys

        :param _dict_book:
        :return:
        """

        return cls(
            title=_dict_book['title'],
            author=_dict_book['author'],
            years=_dict_book['years'],
            id_=_dict_book['id_'],
            reader_id=_dict_book['reader_id'],
        )

    def __str__(self):
        return f'{self.__id}) "{self.__title}". {self.__author}, {self.__years}.'

    def __repr__(self):
        cls_name = __class__.__name__
        return ' '.join(
            [
                f'{attr.replace(f"_{cls_name}__", "")}={getattr(self, attr)}'
                for attr in dir(self) if attr.startswith(f'_{cls_name}__')
            ]
        )