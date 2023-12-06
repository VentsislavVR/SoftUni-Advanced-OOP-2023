from unittest import TestCase,main

from project.library import Library
class TestLibrary(TestCase):
    def setUp(self):
        self.library = Library('Name')

    def test_library_raises_error_when_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            library = Library('')
        self.assertEqual("Name cannot be empty string!",
                         str(ve.exception))
    def test_initialization(self):

        self.assertEqual("Name",self.library.name)
        self.assertEqual({},self.library.books_by_authors)
        self.assertEqual({},self.library.readers)

    def test_add_book_should_add_author_and_title(self):
        author = 'Bob'
        first = 'Title1'
        second = 'Title2'

        self.library.add_book('Bob', 'Title1')
        self.library.add_book('Bob', 'Title2')

        self.assertEqual(1,len(self.library.books_by_authors))
        self.library.add_book('Rob', 'Title3')
        self.assertEqual(2, len(self.library.books_by_authors))

        self.assertTrue(author in self.library.books_by_authors)

        self.assertEqual([first,second],self.library.books_by_authors[author])

    def test_add_reader_successfully(self):
        self.assertEqual(0,len(self.library.readers))
        self.library.add_reader('Reader')

        self.assertEqual(1, len(self.library.readers))
        self.assertTrue('Reader' in self.library.readers)
        self.assertEqual([],self.library.readers['Reader'])



    def test_add_reader_unsuccessfully(self):
        self.library.add_reader('Reader')
        result = self.library.add_reader('Reader')
        self.assertEqual(f"Reader is already registered in the Name library.",
                         result)

    def test_rent_book_not_registered_reader(self):
        result = self.library.rent_book('Reader','Bob','Title1')
        self.assertEqual(f"Reader is not registered in the Name Library.",result)

    def test_rent_book_book_not_in_library(self):
        reader = 'reader'
        author = 'bob'


        self.library.add_reader(reader)
        result = self.library.rent_book(reader,author,'title')
        self.assertEqual(f"Name Library does not have any {author}'s books.",result)

    def test_rent_book_title_not_in_library(self):
        reader = 'reader'
        author = 'bob'
        title = 'title'

        self.library.add_reader(reader)
        self.library.add_book('author',title)

        result = self.library.rent_book(reader,author,title)
        self.assertEqual(f"""Name Library does not have {author}'s "book".""",result)

    def test_rent_book_success(self):
        reader = 'reader'
        author = 'bob'
        title = 'title'
        title2 = 'title2'
        self.library.add_reader(reader)
        self.library.add_book(author, title)
        self.library.add_book(author, title2)

        self.library.rent_book(reader, author, title)

        self.assertEqual([{author:title}],self.library.readers[reader])
        self.assertEqual(1,len(self.library.books_by_authors[author]))
        self.assertTrue(title not in self.library.books_by_authors[author])
        self.assertTrue(title2 in self.library.books_by_authors[author])




if __name__ == '__main__':
    main()