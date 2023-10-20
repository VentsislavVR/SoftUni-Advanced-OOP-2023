def movie_organizer(*args):
    collection = {}
    for movie_name, genre in args:
        if genre not in collection:
            collection[genre] = []
        collection[genre].append(movie_name)
    result = ''
    sorted_movie_collection = sorted(collection.items(),key=lambda kvp: (-len(kvp[1]),kvp[0]))
    for genre,movies in sorted_movie_collection:
        result +=f'{genre} - {len(movies)}\n'
        for movie in sorted(movies):
            result +=f"* {movie}\n"

    return result


from unittest import TestCase, main


class Test(TestCase):
    def test_movie_organizer(self):
        result = movie_organizer(("The Matrix", "Sci-fi"))

        self.assertEqual(
            result.strip(),
            """Sci-fi - 1
* The Matrix""")


if __name__ == '__main__':
    main()