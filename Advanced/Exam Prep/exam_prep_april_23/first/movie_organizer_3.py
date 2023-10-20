def movie_organizer(*args):
    organizer = {}
    for movie, genre in args:
        if genre not in organizer:
            organizer[genre] = {
                'movies': [],
                'count': 0
            }
        organizer[genre]['movies'].append(movie)
        organizer[genre]['count'] = len(organizer[genre]['movies'])
    sorted_organizer = sorted(organizer.items(), key=lambda x: (-x[1]['count'], x[0]))
    result = []
    for k, v in sorted_organizer:
        result.append(f"{k} - {v['count']}\n")
        for movie in sorted(v['movies']):
            result.append(f"* {movie}\n")

    return ''.join(result)


from unittest import TestCase, main


class Test(TestCase):
    def test_movie_organizer(self):
        result = movie_organizer(("The Godfather", "Drama"),
                                 ("The Hangover", "Comedy"),
                                 ("The Shawshank Redemption", "Drama"),
                                 ("The Pursuit of Happiness", "Drama"),
                                 ("The Hangover Part II", "Comedy")
                                 )

        self.assertEqual(
            result.strip(),
            """Drama - 3
* The Godfather
* The Pursuit of Happiness
* The Shawshank Redemption
Comedy - 2
* The Hangover
* The Hangover Part II""")


if __name__ == '__main__':
    main()
