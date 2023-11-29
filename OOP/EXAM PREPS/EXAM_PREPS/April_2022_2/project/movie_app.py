from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def register_user(self, username: str, age: int):
        ...

    def upload_movie(self, username: str, movie: Movie):
        ...

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        ...

    def delete_movie(self, username: str, movie: Movie):
        ...

    def like_movie(self, username: str, movie: Movie):
        ...

    def dislike_movie(self, username: str, movie: Movie):
        ...

    def display_movies(self):
        ...

    def __str__(self):
        ...
