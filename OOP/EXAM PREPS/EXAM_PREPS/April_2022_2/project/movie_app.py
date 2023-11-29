from typing import List, Optional

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def get_registered_users(self, username) -> Optional[User]:
        existing_user = [u for u in self.users_collection if u.username == username]
        if existing_user:
            return existing_user[0]
        return None

    def get_movie(self, title: str) -> Optional[Movie]:
        existing_movie = [m for m in self.movies_collection if m.title == title]
        if existing_movie:
            return existing_movie[0]
        return None

    def register_user(self, username: str, age: int):
        existing_user = self.get_registered_users(username)
        if existing_user:
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):

        existing_user = self.get_registered_users(username)

        if not existing_user:
            raise Exception("This user does not exist!")

        if movie.owner.username != existing_user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        existing_movie = self.get_movie(movie.title)
        if existing_movie:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        existing_user.movies_owned.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        existing_user = self.get_registered_users(username)
        existing_movie = self.get_movie(movie.title)

        if not existing_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            # if hasattr(movie, key):
            setattr(movie, key, value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):

        existing_user = self.get_registered_users(username)
        existing_movie = self.get_movie(movie.title)

        if not existing_movie:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner "
                            f"of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        existing_user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        existing_user = self.get_registered_users(username)

        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in existing_user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        existing_user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        existing_user = self.get_registered_users(username)

        if movie not in existing_user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        existing_user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        result = sorted(self.movies_collection, key=lambda movie: (-movie.year, movie.title))

        return '\n'.join([x.details() for x in result]) if result else "No movies found."

    def __str__(self):
        result = ["All users: No users."
                  if not self.users_collection else
                  "All users: "
                  +
                  ', '.join(u.username for u in self.users_collection), "All movies: No movies."
                  if not self.movies_collection else
                  "All movies: "
                  +
                  ', '.join(m.title for m in self.movies_collection)]

        return '\n'.join(result)
