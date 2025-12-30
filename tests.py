from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    def test_add_new_book_add_duplicate(self):
        collector = BooksCollector()

        collector.add_new_book('Человек, который смеется')
        collector.add_new_book('Человек, который смеется')

        assert collector.get_books_genre() == {'Человек, который смеется': ''}

    @pytest.mark.parametrize('name', ['', 'Человек, который смеется и не только смеется'])
    def test_add_new_book_not_add_invalid_name(self, name):
        collector = BooksCollector()

        collector.add_new_book(name)

        assert collector.get_books_genre() == {}

    def test_set_book_genre_for_existing_book(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_book_genre('Дюна') == 'Фантастика'

    def test_set_book_genre_invalid_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Поющие в терновнике')
        collector.set_book_genre('Поющие в терновнике', 'Романтика')

        assert collector.get_book_genre('Поющие в терновнике') == ''

    def test_get_book_genre_returns_genre_for_existing_book(self):
        collector = BooksCollector()

        collector.add_new_book('Иллюминэ')
        collector.set_book_genre('Иллюминэ', 'Фантастика')

        assert collector.get_book_genre('Иллюминэ') == 'Фантастика'

    def test_get_book_genre_returns_none_for_nonexistent_book(self):
        collector = BooksCollector()

        assert collector.get_book_genre('Неизвестная книга') is None

    @pytest.mark.parametrize(
            'books_with_genres, genre, expected',
            [
                (
                    {
                        "1984": "Фантастика",
                        "Шерлок Холмс": "Детективы",
                        "Имя розы": "Детективы",
                    },
                    "Детективы",
                    ["Шерлок Холмс", "Имя розы"],
                ),
                (
                    {
                        "1984": "Фантастика",
                    },
                    "Фантастика",
                    ["1984"],
                )
            ],
    )
    def test_get_books_with_specific_genre_returns_expected_books(self, books_with_genres, genre, expected):
        collector = BooksCollector()

        for book,book_genre in books_with_genres.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, book_genre)

        assert collector.get_books_with_specific_genre(genre) == expected

    def test_get_books_genre_returns_full_dict(self):
        collector = BooksCollector()

        collector.add_new_book('Солярис')
        collector.set_book_genre('Солярис', 'Фантастика')

        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Десять негритят', 'Детективы')

        assert collector.get_books_genre() == {
            'Солярис': 'Фантастика',
            'Десять негритят': 'Детективы'
        }

    @pytest.mark.parametrize( 
            "books, expected_children_books",
            [
                ([("Марсианин","Фантастика"), ("Оно","Ужасы"), ("Дракула","Ужасы и не только")], ["Марсианин"]),
                ([("Гарри Поттер","Фантастика")], ["Гарри Поттер"]),
                ([("Оно","Ужасы")], []),
            ]
        )
    def test_get_books_for_children_returns_only_allowed_books(self, books, expected_children_books):
        collector = BooksCollector()
        
        for name, genre in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        assert collector.get_books_for_children() == expected_children_books

    def test_add_book_in_favorites_adds_book(self):
        collector = BooksCollector()

        collector.add_new_book('День триффидов')
        collector.add_book_in_favorites('День триффидов')

        assert collector.get_list_of_favorites_books() == ['День триффидов']

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()

        collector.add_new_book('День триффидов')
        collector.add_book_in_favorites('День триффидов')

        collector.delete_book_from_favorites('День триффидов')

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_empty_by_default(self):
        collector = BooksCollector()

        assert collector.get_list_of_favorites_books() == []
