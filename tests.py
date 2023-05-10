from main import BooksCollector


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
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # добавление дубликата в коллекцию
    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book('Игра Престолов')
        collector.add_new_book('Игра Престолов')
        assert len(collector.get_books_rating()) == 1
    #добавление книги и установление рейтинга, и получение рейтинга через get_bool_rating
    def test_set_book_rating_valid_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Игра Престолов')
        collector.set_book_rating('Игра Престолов', 5)
        assert collector.get_book_rating('Игра Престолов') == 5
# Нельзя выставить рейтинг книге, которой нет в списке
    def test_set_book_rating_invalid_book(self):
        collector = BooksCollector()
        collector.set_book_rating('Игра Престолов', 5)
        assert collector.get_book_rating('Игра Престолов') is None

    #нельзя выставить рейтинг меньше 1 и больше 10, условия такие, если не указывает рейтинг, то он по априори 1
    def test_set_book_rating_invalid_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_rating('Гордость и предубеждение', -1)
        assert collector.get_book_rating('Гордость и предубеждение') == 1
        collector.set_book_rating('Гордость и предубеждение', 11)
        assert collector.get_book_rating('Гордость и предубеждение') == 1

    #У книги нет рейтинга, так как ее нет в списке
    def test_get_book_rating_non_existent_book(self):
        collector = BooksCollector()
        assert collector.get_book_rating('Гордость и предубеждение') is None

    def test_get_books_with_specific_rating(self):
        collector = BooksCollector()
        collector.add_new_book('1984')
        collector.set_book_rating('1984', 8)

        collector.add_new_book('Мастер и Маргарита')
        collector.set_book_rating('Мастер и Маргарита', 7)

        collector.add_new_book('Преступление и наказание')
        collector.set_book_rating('Преступление и наказание', 8)

        # Книг с рейтингом 9 нет в списке
        assert collector.get_books_with_specific_rating(9) == []

        # Книг с рейтингом 8 - две книги
        assert collector.get_books_with_specific_rating(8) == ['1984', 'Преступление и наказание']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('1984')

        # добавляем первую книгу в избранное
        collector.add_book_in_favorites('Мастер и Маргарита')

        # проверяем, что книга добавилась в список избранных
        assert collector.get_list_of_favorites_books() == ['Мастер и Маргарита']

        # пытаемся добавить в избранное несуществующую книгу
        collector.add_book_in_favorites('Война и мир')

        # проверяем, что книга не добавилась в список избранных
        assert collector.get_list_of_favorites_books() == ['Мастер и Маргарита']

        # добавляем вторую книгу в избранное
        collector.add_book_in_favorites('1984')

        # проверяем, что в список избранных добавилась вторая книга
        assert collector.get_list_of_favorites_books() == ['Мастер и Маргарита', '1984']

        # добавляем еще раз первую книгу в избранное
        collector.add_book_in_favorites('Мастер и Маргарита')

        # проверяем, что первая книга уже была в списке избранных и повторно не добавляется
        assert collector.get_list_of_favorites_books() == ['Мастер и Маргарита', '1984']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        book_name = 'Гарри Поттер и философский камень'
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)

        # Проверяем, что книга добавлена в список избранных
        assert book_name in collector.get_list_of_favorites_books()

        collector.delete_book_from_favorites(book_name)

        # Проверяем, что книга удалена из списка избранных
        assert book_name not in collector.get_list_of_favorites_books()

