import pytest


@pytest.fixture
def clear_books_database():
    print("[FIXTURE] Delete data from database")


@pytest.fixture
def fill_books_database():
    print("[FIXTURE] Create data in database")


@pytest.mark.usefixtures('fill_books_database')
def test_read_all_books_in_library(clear_books_database):
    print("Reading all books")


@pytest.mark.usefixtures(
    'fill_books_database',
    'clear_books_database')
class TestLibrary:
    @pytest.mark.usefixtures('fill_books_database')
    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...
