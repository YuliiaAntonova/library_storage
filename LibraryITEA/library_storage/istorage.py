from abc import ABC, abstractmethod
from ..library_units.book import Book
from ..library_units.reader import Reader

import os
from ..utils import logprint


class IStorage(ABC):
    """Abstract class which describe IStorage"""

    @abstractmethod
    def load_books(self) -> list:
        pass

    @abstractmethod
    def load_readers(self) -> list:
        pass

    @abstractmethod
    def save_books(self, books: list):
        pass

    @abstractmethod
    def save_readers(self, readers: list):
        pass


    # @abstractmethod
    # def add_book(self, obj_book: Book) -> bool:
    #     pass
    #
    # @abstractmethod
    # def remove_book(self, obj_book: Book) -> bool:
    #     pass
    #
    # @abstractmethod
    # def update_book(self, obj_book: Book) -> bool:
    #     pass
    #
    # @abstractmethod
    # def add_reader(self, obj_reader: Reader) -> bool:
    #     pass
    #
    # @abstractmethod
    # def remove_reader(self, obj_reader: Reader) -> bool:
    #     pass
    #
    # @abstractmethod
    # def update_reader(self, obj_reader: Reader) -> bool:
    #     pass

    @staticmethod
    def load_books_from_txt_file(filename: str,
                                 sep: str = ',',
                                 encoding: str = 'utf-8') -> list:
        """
        returns a new dictionary with the passed memories as keys

        :param: filename
        :return: list
        """

        res_book_list = []

        if not os.path.exists(filename):
            logprint.print_fail(f'File \'{filename}\' not found!')
            return res_book_list

        with open(filename, encoding=encoding) as file:
            for line in file:
                line_list = line.strip().split(sep)
                res_book_list.append(Book(
                    line_list[0],       # title
                    line_list[1],       # author
                    int(line_list[2]),  # years
                ))

        return res_book_list

    @staticmethod
    def load_readers_from_txt_file(filename: str,
                                   sep: str = ',',
                                   encoding: str = 'utf-8') -> list:
        """
          returns a new dictionary with the passed memories as keys

          :param: filename
          :return: list
              """
        _res_readers_list = []

        if not os.path.exists(filename):    # access file on exist
            logprint.print_fail(f'file \'{filename}\' not found!')
            return _res_readers_list

        with open(filename, encoding=encoding) as _file:
            for _line in _file:
                _line_list = _line.strip().split(sep)
                _res_readers_list.append(Reader(
                    _line_list[0],      # name
                    _line_list[1],      # surname
                    int(_line_list[2])  # years
                ))

        return _res_readers_list
