import logging
import pytest
from io import StringIO
from goit_pythonweb_hw_01.library_management import Library, LibraryManager, Book


@pytest.fixture
def caplog():
    stream = StringIO()
    handler = logging.StreamHandler(stream)
    logger = logging.getLogger("LibraryManagementLogger")
    logger.addHandler(handler)
    yield stream
    logger.removeHandler(handler)


def test_add_book(caplog):
    library = Library()
    book = Book("1984", "George Orwell", 1949)

    library.add_book(book)

    assert (
        "Book added: Title: 1984, Author: George Orwell, Year: 1949"
        in caplog.getvalue()
    )
    assert len(library.books) == 1


def test_remove_book_existing(caplog):
    library = Library()
    book = Book("1984", "George Orwell", 1949)
    library.add_book(book)

    library.remove_book("1984")

    assert "Book removed: 1984" in caplog.getvalue()
    assert len(library.books) == 0


def test_remove_book_non_existing(caplog):
    library = Library()

    library.remove_book("Some name")

    assert "Book not found: Some name" in caplog.getvalue()


def test_show_books_empty(caplog):
    library = Library()

    library.show_books()

    assert "No books in the library." in caplog.getvalue()


def test_show_books_with_books(caplog):
    library = Library()
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("Brave New World", "Aldous Huxley", 1932)

    library.add_book(book1)
    library.add_book(book2)

    library.show_books()

    assert "Title: 1984, Author: George Orwell, Year: 1949" in caplog.getvalue()
    assert (
        "Title: Brave New World, Author: Aldous Huxley, Year: 1932" in caplog.getvalue()
    )


def test_library_manager_add_book(caplog):
    library = Library()
    manager = LibraryManager(library)

    manager.add_book("1984", "George Orwell", 1949)

    assert (
        "Book added: Title: 1984, Author: George Orwell, Year: 1949"
        in caplog.getvalue()
    )
    assert len(library.books) == 1


def test_library_manager_remove_book(caplog):
    library = Library()
    manager = LibraryManager(library)

    manager.add_book("1984", "George Orwell", 1949)
    manager.remove_book("1984")

    assert "Book removed: 1984" in caplog.getvalue()
    assert len(library.books) == 0


def test_library_manager_show_books(caplog):
    library = Library()
    manager = LibraryManager(library)

    manager.add_book("1984", "George Orwell", 1949)
    manager.add_book("Brave New World", "Aldous Huxley", 1932)

    manager.show_books()

    assert "Title: 1984, Author: George Orwell, Year: 1949" in caplog.getvalue()
    assert (
        "Title: Brave New World, Author: Aldous Huxley, Year: 1932" in caplog.getvalue()
    )
