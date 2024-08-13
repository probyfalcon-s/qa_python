import pytest

from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить', 'Ржи во ржи', 'Ешь Люби Спи'])
    def test_add_new_book_true(self, name):  # 1
        collector = BooksCollector()
        collector.add_new_book(name)
        assert collector.books_genre.get(name) == ''

    @pytest.mark.parametrize('name', ['Ржи во ржи', 'Ешь Люби Спи', '273 градуса по Кельвину слева'])
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_true(self, name, genre):  # 2
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.books_genre.get(name) == genre

    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_book_genre_true(self, name, genre): #3
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre_books_empty_list(self, name, genre): #4
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_new_book(name)
        books_with_genre = collector.get_books_with_specific_genre(genre)
        assert books_with_genre == []

    def test_get_books_with_specific_genre_books_list(genre): #4_1
        collector = BooksCollector()
        collector.genre = ['Ужасы', 'Детективы']
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
        books_with_genre = collector.get_books_with_specific_genre('Ужасы')
        assert books_with_genre == ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить']


    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_genre_true(self, name, genre): #5
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        collector.get_books_genre()
        assert genre in collector.genre

    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_for_children_empty_list(self, name, genre): #6_1
        collector = BooksCollector()
        collector.genre = [name, genre]
        collector.add_new_book(name)
        collector.add_new_book(name)
        books_with_genre_for_children = collector.get_books_for_children()
        assert books_with_genre_for_children == []

    def test_get_books_for_children_list(genre): #6
        collector = BooksCollector()
        collector.genre = ['Фантастика', 'Мультфильмы', 'Комедии']
        collector.add_new_book('Вниз')
        collector.add_new_book('Животнополис')
        collector.set_book_genre('Вниз', 'Мультфильмы')
        collector.set_book_genre('Животнополис', 'Мультфильмы')
        books_with_genre = collector.get_books_for_children()
        assert books_with_genre == ['Вниз', 'Животнополис']

    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    def test_add_book_in_favorites_true(self, name): #7
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.favorites

    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    def test_delete_book_from_favorites_true(self, name): #8
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites

    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить'])
    def test_get_list_of_favorites_books_list(self, name): #9
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert name, name in collector.favorites