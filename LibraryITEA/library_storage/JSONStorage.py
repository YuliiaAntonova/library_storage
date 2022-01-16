import os
import json

from .istorage import IStorage

from ..library_units.book import Book
from ..library_units.reader import Reader

from ..utils import logprint


class JSONStorage(IStorage):
    def __init__(self, db_books_filename, db_readers_filename):
        self.__db_books_filename = db_books_filename
        self.__db_readers_filename = db_readers_filename

    def load_books(self) -> list:
        if not os.path.exists(self.__db_books_filename):
            logprint.print_warning('JSON books database doesn\'t exist yet')
            return []

        with open(self.__db_books_filename) as file:
            dict_books = json.load(file)

        return [
            Book.from_dict(book)
            for book in dict_books
        ]

    def load_readers(self) -> list:
        if not os.path.exists(self.__db_readers_filename):
            logprint.print_warning('JSON readers database doesn\'t exist yet')
            return []

        with open(self.__db_readers_filename) as file:
            dict_readers = json.load(file)                     #return list of dicts from json

        return [
            Reader.from_dict(reader)
            for reader in dict_readers
        ]

    def save_books(self, books: list):
        with open(self.__db_books_filename, 'w') as file:
            json.dump([book.dict() for book in books], file)      #return json

    def save_readers(self, readers: list):
        with open(self.__db_readers_filename, 'w') as file:
            json.dump([ reader.dict() for reader in readers ], file)