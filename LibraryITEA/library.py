from .library_units.book import Book
from .library_units.reader import Reader
from .library_storage.istorage import IStorage

from .utils import logprint

from typing import Union


class Library:
    def __init__(self, storage: IStorage,
                 books: list = None,
                 readers: list = None):

        self.__storage = storage

        self.__books = books if books else []
        self.__readers = readers if readers else []

    # INIT
    ###################################################################################################
    def load_books(self) -> bool:
        self.__books = self.__storage.load_books()
        if len(self.__books):
            return True
        return False

    def load_readers(self) -> bool:
        self.__readers = self.__storage.load_readers()
        if len(self.__readers):
            return True
        return False

    def load_books_from_txt_file(self, filename: str,
                                 sep: str = ',',
                                 encoding: str = 'utf-8') -> bool:
        self.__books = self.__storage.load_books_from_txt_file(filename, sep, encoding)
        if not len(self.__books):
            logprint.print_fail(f'error load books from \'{filename}\'')
            return False

        self.save_all_books()
        return True

    def load_readers_from_txt_file(self, filename: str,
                                   sep: str = ',',
                                   encoding: str = 'utf-8') -> bool:
        self.__readers = self.__storage.load_readers_from_txt_file(filename, sep, encoding)
        if not len(self.__readers):
            logprint.print_fail(f'error load readers from {filename}')
            return False

        self.save_all_readers()
        return True
    ###################################################################################################

    # GIVE - RETURN
    ###################################################################################################
    def give_book(self, book_id: int, reader_id: int) -> (bool, str):
        return_msg = ''

        book = self.__get_book_by_id(book_id)
        if not book:
            return_msg = f'book with id {book_id} is not in the library'
            logprint.print_fail(return_msg)
            return False, return_msg

        reader = self.__get_reader_by_id(reader_id)
        if not reader:
            return_msg = f'reader with id {reader_id} is not in the library'
            logprint.print_fail(return_msg)
            return False, return_msg

        if book.get_reader_id() is not None:
            return_msg = f'book with id {book_id} are out of stock'
            logprint.print_fail(return_msg)
            return False, return_msg

        book.set_reader_id(reader_id)

        # todo: применить при переходе на SQL
        # self.__storage.update_book(book)
        self.save_all_books()

        return_msg = f'book with id {book_id} have been successfully issued to the reader with id {reader_id}'
        logprint.print_done(return_msg)

        return True, return_msg

    def return_book(self, book_id: int, reader_id: int):
        return_msg = ''

        book = self.__get_book_by_id(book_id)
        if not book:
            return_msg = f'book with id {book_id} is not in the library'
            logprint.print_fail(return_msg)
            return False, return_msg

        reader = self.__get_reader_by_id(reader_id)
        if not reader:
            return_msg = f'reader with id {reader_id} is not in the library'
            logprint.print_fail(return_msg)
            return False, return_msg

        if book.get_reader_id() != reader.get_id():
            return_msg = f'book with id {book_id} is not ' \
                         f'in the possession of the reader ' \
                         f'{reader.get_name()} {reader.get_surname()}'
            logprint.print_fail(return_msg)
            return False, return_msg

        book.set_reader_id(None)

        # todo: применить при переходе на SQL
        # self.__storage.update_book(book)
        self.save_all_books()

        return_msg = f'Reader {reader.get_name()} {reader.get_surname()} ' \
                     f'returned the book "{book.get_title()}" to the library'
        logprint.print_done(return_msg)

        return True, return_msg
    ###################################################################################################

    # BOOKS
    ###################################################################################################
    def add_book(self, title: str, author: str, year: int, book_id: int = None) -> str:
        # if book_id in [book.get_id() for book in self.__books]

        if book_id is not None:
            for book in self.__books:
                if book.get_id() == book_id:
                    return f'Error: book with id {book_id} already exists'

        _book = Book(title, author, year, book_id)
        self.__books.append(_book)

        # self.__storage.add_book(_book)
        self.save_all_books()

        return f'Done: book was successfully added to the library'

    # todo: def remove_book(self, id: int) -> bool:

    def get_all_books(self) -> list:
        return self.__books

    def get_available_books(self):
        return [book for book in self.__books if not book.get_reader_id()]

    def get_unavailable_books(self):
        return [book for book in self.__books if book.get_reader_id()]

    def print_sorted_book(self, sort: str = 'id', reverse: bool = False):
        if sort not in ['id', 'title', 'year']:
            print(f'Error: no sorting by {sort} field')
            return

        def get_sort_field(book: Book):
            if sort == 'id': return book.get_id()
            elif sort == 'title': return book.get_title()
            elif sort == 'year': return book.get_years()

        for book in sorted(self.__books, key=get_sort_field, reverse=reverse):
            print(book)

    def __get_book_by_id(self, book_id: int) -> Union[Book, None]:
        """
        Функция получения книги по id из списка книг

        :param book_id: id книги, которую хотим получить
        :return: obj Book (если книга есть в библиотеке); None (если книги нет)
        """
        for book in self.__books:
            if book.get_id() == book_id:
                return book
        return None
    ###################################################################################################

    # READERS
    ###################################################################################################
    def add_reader(self, name: str, surname: str, year: int, reader_id: int = None) -> str:
        if reader_id is not None:
            for reader in self.__readers:
                if reader.get_id() == reader_id:
                    return f'Error: reader with id {reader_id} already exists'

        self.__readers.append(Reader(name, surname, year, reader_id))
        return f'Done: reader was successfully added to the library'

    # todo: def remove_reader(self, id: int) -> bool:

    def get_all_readers(self):
        return self.__readers

    def __get_reader_by_id(self, reader_id: int) -> Union[Reader, None]:
        """
        Функция получения читателя по id из списка читателей

        :param reader_id: id читателя
        :return: obj Reader (если читатель есть в библиотеке); None (если читателя нет)
        """
        for reader in self.__readers:
            if reader.get_id() == reader_id:
                return reader
        return None
    ###################################################################################################

    # OTHER
    ###################################################################################################
    def save_all_books(self):
        self.__storage.save_books(self.__books)

    def save_all_readers(self):
        self.__storage.save_readers(self.__readers)
    ###################################################################################################
