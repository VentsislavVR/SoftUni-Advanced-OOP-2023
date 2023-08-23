from project.bookstore import Bookstore

from unittest import TestCase, main


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.store = Bookstore(15)

    def test_initialization(self):
        self.assertEqual(15, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test_negative_book_limit_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = -1
        self.assertEqual(f"Books limit of -1 is not valid",
                          str(ve.exception))

    def test__len__books(self):
        self.assertEqual(0, len(self.store))
        self.store.availability_in_store_by_book_titles['book'] = 1
        self.assertEqual(1, len(self.store))
        self.store.availability_in_store_by_book_titles['book2'] = 2
        self.assertEqual(3, len(self.store))

    def test_receive_book_over_limit_raises(self):
        with self.assertRaises(Exception) as ex:
            self.store.availability_in_store_by_book_titles['book'] = 14
            self.store.receive_book("book2", 4)
        self.assertEqual("Books limit is reached. Cannot receive more books!",
                          str(ex.exception))

    def test_receive_new_book(self):
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)

        result = self.store.receive_book('book', 10)

        self.assertEqual({'book': 10}, self.store.availability_in_store_by_book_titles)

        self.assertEqual(f"10 copies of book are available in the bookstore.",
                          result)
    def test_existing_book(self):
        self.store.availability_in_store_by_book_titles={'book':5}
        resulr = self.store.receive_book('book',5)
        self.assertEqual(f"10 copies of book are available in the bookstore.",
        resulr)


    def test_sell_non_existing_book_raises(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book("book", 10)
        self.assertEqual(f"Book book doesn't exist!",
                          str(ex.exception))

    def test_try_to_sell_more_than_available(self):
        self.store.receive_book('book', 10)

        with self.assertRaises(Exception) as ex:
            self.store.sell_book('book', 12)
        self.assertEqual(f"book has not enough copies to sell. Left: 10",
                          str(ex.exception))

    def test_successful_sell(self):
        self.store.receive_book('book', 10)
        result = self.store.sell_book('book', 5)

        self.assertEqual(f"Sold 5 copies of book",
                          result)
        self.assertEqual(5,self.store.total_sold_books)

    def test__str__(self):
        self.store.availability_in_store_by_book_titles ={
            'book':1,
            'book2':1
        }
        self.assertEqual(
        f"Total sold books: 0\n"
            f"Current availability: 2\n"
            " - book: 1 copies\n"
            " - book2: 1 copies",
            str(self.store)
        )


if __name__ == '__main__':
    main()
