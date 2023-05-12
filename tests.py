from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Игра Престолов')
        collector.add_new_book('Игра Престолов')
        assert len(collector.get_books_rating()) == 1, 'Ошибка! Книга уже была добавлена'

    def test_set_book_rating_valid_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Игра Престолов')
        collector.set_book_rating('Игра Престолов', 5)
        assert collector.get_book_rating('Игра Престолов') == 5

    def test_set_book_rating_invalid_book(self):
        collector = BooksCollector()
        collector.set_book_rating('Игра Престолов', 5)
        assert collector.get_book_rating('Игра Престолов') is None

    def test_set_book_rating_invalid_rating_minus1(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_rating('Гордость и предубеждение', -1)
        assert collector.get_book_rating('Гордость и предубеждение') == 1

    def test_set_book_rating_invalid_rating_plus11(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_rating('Гордость и предубеждение', 11)
        assert collector.get_book_rating('Гордость и предубеждение') == 1

    def test_get_book_rating_non_existent_book(self):
        collector = BooksCollector()
        assert collector.get_book_rating('Гордость и предубеждение') is None

    def test_get_books_with_specific_rating_not_list(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_rating('1984', 8)

        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_rating('Мастер и Маргарита', 7)

        collector.add_new_book('Преступление и наказание')
        collector.set_book_rating('Преступление и наказание', 8)
        assert collector.get_books_with_specific_rating(9) == []

    def test_get_books_with_specific_rating_valid(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_rating('1984', 8)

        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_rating('Мастер и Маргарита', 7)

        collector.add_new_book('Преступление и наказание')
        collector.set_book_rating('Преступление и наказание', 8)
        assert collector.get_books_with_specific_rating(8) == ['1984', 'Преступление и наказание']

    def test_add_book_in_favorites_valid(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('1984')
        collector.add_book_in_favorites('Мастер и Маргарита')
        assert collector.get_list_of_favorites_books() == ['Мастер и Маргарита']

    def test_add_book_in_favorites_without_add(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('1984')
        collector.add_book_in_favorites('Мастер и Маргарита')
        collector.add_book_in_favorites('Война и мир')
        assert collector.get_list_of_favorites_books() == ['Мастер и Маргарита']

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        collector.add_book_in_favorites('Мастер и Маргарита')
        assert collector.get_list_of_favorites_books() == ['Мастер и Маргарита']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер и философский камень'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()


