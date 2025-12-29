# qa_python

### Тесты на методы `BooksCollector`

1. **Добавление книг (`add_new_book`)**
   - `test_add_new_book_add_duplicate` — проверяет, что книга с одинаковым названием не добавляется дважды.
   - `test_add_new_book_not_add_invalid_name` — проверяет, что пустые названия и названия длиной более 40 символов не добавляются (используется параметризация).

2. **Установка жанра книги (`set_book_genre`)**
   - `test_set_book_genre_for_existing_book` — проверка установки жанра для существующей книги.
   - `test_set_book_genre_invalid_genre` — проверка, что нельзя установить жанр, которого нет в списке допустимых.

3. **Получение жанра книги (`get_book_genre`)**
   - `test_get_book_genre_returns_genre_for_existing_book` — проверка, что метод возвращает правильный жанр для существующей книги.
   - `test_get_book_genre_returns_none_for_nonexistent_book` — проверка, что метод возвращает `None` для несуществующей книги.

4. **Получение книг по жанру (`get_books_with_specific_genre`)**
   - `test_get_books_with_specific_genre_returns_correct_list` — проверка, что метод возвращает корректный список книг для указанного жанра. Используется параметризация для нескольких жанров.

5. **Получение полного словаря книг с жанрами (`get_books_genre`)**
   - `test_get_books_genre_returns_full_dict` — проверка, что возвращается полный словарь книг с жанрами.

6. **Книги для детей (`get_books_for_children`)**
   - `test_get_books_for_children_returns_only_allowed_books` — проверка, что возвращаются только книги с жанрами, разрешёнными для детей. Используется параметризация для нескольких наборов книг.

7. **Работа с избранным (`add_book_in_favorites`, `delete_book_from_favorites`, `get_list_of_favorites_books`)**
   - `test_add_book_in_favorites_adds_book` — проверка добавления существующей книги в избранное.
   - `test_delete_book_from_favorites_removes_book` — проверка удаления книги из избранного.
   - `test_get_list_of_favorites_books_returns_empty_by_default` — проверка, что у нового экземпляра `BooksCollector` список избранных пуст.
