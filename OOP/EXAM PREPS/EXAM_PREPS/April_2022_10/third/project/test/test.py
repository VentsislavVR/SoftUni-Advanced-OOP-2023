from unittest import TestCase

from project.movie import Movie



class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie('8 mile',2002,10)

    def test_correct_initialization(self):
        self.assertEqual('8 mile', self.movie.name)
        self.assertEqual(2002,self.movie.year)
        self.assertEqual(10, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_set_name_to_empty_string_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''
        self.assertEqual('Name cannot be an empty string!',str(ve.exception))

    def test_year_to_1886_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!",str(ve.exception))

    def test_add_actor_unique(self):
        self.assertEqual([],self.movie.actors)
        self.movie.add_actor('Slim S')
        self.assertEqual(1,len(self.movie.actors))
        self.assertEqual(['Slim S'], self.movie.actors)


    def test_add_existing_actor_expect_exception(self):
        self.movie.add_actor('Slim S')
        result=self.movie.add_actor('Slim S')
        self.assertEqual("Slim S is already added in the list of actors!", result)

    def test_rating_first_movie_gt_second_returns_str(self):
        new_movie = Movie('Elvis',2022,9.5)

        result = self.movie > new_movie
        self.assertEqual('"8 mile" is better than "Elvis"', result)

    def test_rating_second_movie_gt_first_returns_str(self):
        new_movie = Movie('Elvis',2022,9.5)

        result = new_movie> self.movie
        self.assertEqual('"8 mile" is better than "Elvis"', result)

    def test_rpr(self):
        self.movie.add_actor('Slim S')
        self.movie.add_actor('50 cent')

        expected = f"Name: 8 mile\n" \
               f"Year of Release: 2002\n" \
               f"Rating: 10.00\n" \
               f"Cast: Slim S, 50 cent"
        result = self.movie.__repr__()
        self.assertEqual(expected,result)
