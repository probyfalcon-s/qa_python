import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(name):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    #@pytest.mark.parametrize('name,genre',['Ржи во ржи', 'Ешь Люби Спи', '273 градуса по Кельвину слева'])
    def test_add_new_book_true(name): #1
        collector = BooksCollector()
        collector.add_new_book('Ржи во ржи')
        assert collector.books_genre['Ржи во ржи'] == ''

    def test_set_book_genre_true(name): #2
        collector = BooksCollector()
        collector.add_new_book('Ешь Люби Спи')
        collector.set_book_genre('Ешь Люби Спи', 'Фантастика')
        assert collector.books_genre['Ешь Люби Спи'] == 'Фантастика'

    def test_get_book_genre_true(name): #3
        collector = BooksCollector()
        collector.add_new_book('273 градуса по Кельвину слева')
        collector.set_book_genre('273 градуса по Кельвину слева', 'Фантастика')
        assert collector.get_book_genre('273 градуса по Кельвину слева') == 'Фантастика'

    def test_get_books_with_specific_genre_books_list(genre): #4
        collector = BooksCollector()
        collector.add_new_book('Book1')
        collector.add_new_book('Book2')
        books_with_genre = collector.get_books_with_specific_genre('Ужасы')
        assert books_with_genre == [] #пустой список
        #assert books_with_genre == ['Book1', 'Book2'] #Список с книгами

    def test_get_books_genre_true(name): #5 not_pass
        collector = BooksCollector()
        collector.add_new_book('Ржи во ржи')
        collector.set_book_genre('Ржи во ржи', 'Фантастика')
        collector.get_books_genre()
        assert 'Фантастика' in collector.genre

    def test_get_books_for_children_list(genre): #6
        collector = BooksCollector()
        collector.genre = ['Мультфильмы', 'Приключения']
        collector.add_new_book('Book1')
        collector.add_new_book('Book2')
        books_with_genre_for_children = collector.get_books_for_children()
        assert books_with_genre_for_children == [] #пустой список
        #assert books_with_genre_for_children == ['Book1', 'Book2'] #Список с книгами

    def test_add_book_in_favorites_true(name):
        collector = BooksCollector()
        collector.add_new_book('Book1')
        collector.add_book_in_favorites('Book1')
        assert 'Book1' in collector.favorites

    def test_delete_book_from_favorites_true(name):
        collector = BooksCollector()
        collector.add_new_book('Book1')
        collector.delete_book_from_favorites('Book1')
        assert 'Book1' not in collector.favorites

    def test_get_list_of_favorites_books_list(name):
        collector = BooksCollector()
        collector.add_new_book('Book1')
        collector.add_new_book('Book2')
        collector.add_book_in_favorites('Book1')
        collector.add_book_in_favorites('Book2')
        assert 'Book1', 'Book2' in collector.favorites