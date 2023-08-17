from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie = Movie("8 Mile", 2002, 10)

    def test_correct_initialization(self):
        self.assertEqual("8 Mile", self.movie.name)
        self.assertEqual(2002, self.movie.year)
        self.assertEqual(10, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_proper_name_set(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''

        self.assertEqual("Name cannot be an empty string!",
                         str(ve.exception))

    def test_check_if_year_is_valid(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1800
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_adding_existing_actors_to_the_list_of_actors(self):
        self.movie.add_actor("Marshal Mathers")
        result = self.movie.add_actor("Marshal Mathers")

        self.assertEqual(f"Marshal Mathers is already"
                         f" added in the list of actors!"
                         , result)

    def test_add_unique_actor_to_list_of_actors(self):
        self.movie.add_actor("Slim Shady")
        self.assertEqual(["Slim Shady"], self.movie.actors)

    def test_comparing_first_movies_better_by_rating(self):
        new_movie = Movie("Elvis", 2022, 9.5)

        result = self.movie > new_movie
        self.assertEqual(f'"{self.movie.name}" is better than "{new_movie.name}"'
                         , result)

    def test_comparing_second_movie_is_better_by_rating(self):
        new_movie = Movie("Elvis", 2022, 11)

        result = new_movie > self.movie
        self.assertEqual(f'"{new_movie.name}" is better than "{self.movie.name}"'
                         , result)

    def test__repr__(self):
        self.movie.add_actor("Homer")
        self.movie.add_actor("Homer2")
        expected = f"Name: 8 Mile\n" \
                   f"Year of Release: 2002\n" \
                   f"Rating: 10.00\n" \
                   f"Cast: Homer, Homer2"
        result = self.movie.__repr__()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
