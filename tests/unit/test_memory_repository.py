from datetime import date, datetime
from typing import List

import pytest

from movies.domain.model1 import Movie, Genre, Director, Actor, Review, make_review, User
from movies.adapters.repository import RepositoryException


def test_repository_can_add_a_user(in_memory_repo):
    user = User('Dave', '123456789')
    in_memory_repo.add_user(user)

    assert in_memory_repo.get_user('Dave') is user


def test_repository_does_not_retrieve_a_non_existent_user(in_memory_repo):
    user = in_memory_repo.get_user('prince')
    assert user is None


def test_repository_can_retrieve_movie_count(in_memory_repo):
    number_of_movies = in_memory_repo.get_number_of_movies()

    # Check that the query returned 6 Articles.
    assert number_of_movies == 1000


def test_repository_can_add_movie(in_memory_repo):
    movie = Movie(
        "Hello World",
        2020
    )
    in_memory_repo.add_movie(movie)
    assert in_memory_repo.get_movie(1001) is movie


def test_repository_can_retrieve_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(2)
    # Check that the movie has the expected title.
    assert movie.title == 'Prometheus'
    assert movie.genres == [Genre("Adventure"), Genre("Mystery"), Genre("Sci-Fi")]
    assert movie.director == Director("Ridley Scott")
    assert movie.actors == [Actor("Noomi Rapace"), Actor("Logan Marshall-Green"), Actor("Michael Fassbender"), Actor("Charlize Theron")]
    assert movie.year == 2012
    assert len(movie.reviews) == 0

def test_repository_does_not_retrieve_a_non_existent_movie(in_memory_repo):
    movie = in_memory_repo.get_movie(2000)
    assert movie is None


def test_repository_can_retrieve_movies_by_year(in_memory_repo):
    movies = in_memory_repo.get_movies_by_year(2014)

    # Check that the query returned 98 movie_library.
    assert len(movies) == 98


def test_repository_does_not_retrieve_a_movie_when_there_are_no_movies_for_a_given_year(in_memory_repo):
    movies = in_memory_repo.get_movies_by_year(1800)
    assert len(movies) == 0


# def test_repository_can_retrieve_tags(in_memory_repo):
#     tags: List[Tag] = in_memory_repo.get_tags()
#
#     assert len(tags) == 4
#
#     tag_one = [tag for tag in tags if tag.tag_name == 'New Zealand'][0]
#     tag_two = [tag for tag in tags if tag.tag_name == 'Health'][0]
#     tag_three = [tag for tag in tags if tag.tag_name == 'World'][0]
#     tag_four = [tag for tag in tags if tag.tag_name == 'Politics'][0]
#
#     assert tag_one.number_of_tagged_articles == 3
#     assert tag_two.number_of_tagged_articles == 2
#     assert tag_three.number_of_tagged_articles == 3
#     assert tag_four.number_of_tagged_articles == 1


def test_repository_can_get_first_movie(in_memory_repo):
    movie = in_memory_repo.get_first_movie()
    assert movie.title == 'Guardians of the Galaxy'


def test_repository_can_get_last_movie(in_memory_repo):
    movie = in_memory_repo.get_last_movie()
    assert movie.title == 'Nine Lives'


def test_repository_can_get_movies_by_ids(in_memory_repo):
    movies = in_memory_repo.get_movies_by_id([2, 5, 6])

    assert len(movies) == 3
    assert movies[
               0].title == 'Prometheus'
    assert movies[1].title == "Suicide Squad"
    assert movies[2].title == 'The Great Wall'


def test_repository_does_not_retrieve_movie_for_non_existent_id(in_memory_repo):
    movies = in_memory_repo.get_movies_by_id([0, 2, 5000])

    assert len(movies) == 1
    assert movies[
               0].title == 'Prometheus'


def test_repository_returns_an_empty_list_for_non_existent_ids(in_memory_repo):
    movies = in_memory_repo.get_movies_by_id([0, 5000])

    assert len(movies) == 0


def test_repository_returns_movie_ids_for_existing_actor(in_memory_repo):
    movie_ids = in_memory_repo.get_movie_ids_for_actor('Ryan Gosling')
    movie_ids.sort()
    assert movie_ids == [7, 96, 136, 143, 158, 189, 444, 580, 601, 751]


def test_repository_returns_an_empty_list_for_non_existent_actor(in_memory_repo):
    movie_ids = in_memory_repo.get_movie_ids_for_actor('Nina Kashyap')

    assert len(movie_ids) == 0

def test_repository_returns_movie_ids_for_existing_director(in_memory_repo):
    movie_ids = in_memory_repo.get_movie_ids_for_director('Adam McKay')
    movie_ids.sort()
    assert movie_ids == [143, 361, 470, 936]


def test_repository_returns_an_empty_list_for_non_existent_director(in_memory_repo):
    movie_ids = in_memory_repo.get_movie_ids_for_director('Nina Kashyap')

    assert len(movie_ids) == 0

def test_repository_returns_movie_ids_for_existing_genre(in_memory_repo):
    movie_ids = in_memory_repo.get_movie_ids_for_genre('War')
    movie_ids.sort()
    assert movie_ids == [78, 114, 161, 187, 231, 241, 480, 511, 644, 714, 763, 821, 895]


def test_repository_returns_an_empty_list_for_non_existent_genre(in_memory_repo):
    movie_ids = in_memory_repo.get_movie_ids_for_genre('Kashyapism')

    assert len(movie_ids) == 0
#
#
# def test_repository_returns_date_of_previous_article(in_memory_repo):
#     article = in_memory_repo.get_article(6)
#     previous_date = in_memory_repo.get_date_of_previous_article(article)
#
#     assert previous_date.isoformat() == '2020-03-01'
#
#
# def test_repository_returns_none_when_there_are_no_previous_articles(in_memory_repo):
#     article = in_memory_repo.get_article(1)
#     previous_date = in_memory_repo.get_date_of_previous_article(article)
#
#     assert previous_date is None
#
#
# def test_repository_returns_date_of_next_article(in_memory_repo):
#     article = in_memory_repo.get_article(3)
#     next_date = in_memory_repo.get_date_of_next_article(article)
#
#     assert next_date.isoformat() == '2020-03-05'
#
#
# def test_repository_returns_none_when_there_are_no_subsequent_articles(in_memory_repo):
#     article = in_memory_repo.get_article(6)
#     next_date = in_memory_repo.get_date_of_next_article(article)
#
#     assert next_date is None
#
#
# def test_repository_can_add_a_tag(in_memory_repo):
#     tag = Tag('Motoring')
#     in_memory_repo.add_tag(tag)
#
#     assert tag in in_memory_repo.get_tags()


def test_repository_can_add_a_review(in_memory_repo):
    user = User('Nina', '123456789')
    in_memory_repo.add_user(user)
    user = in_memory_repo.get_user('Nina')
    movie = in_memory_repo.get_movie(2)
    review = make_review(review_text="This movie was average", user=user, movie= movie)

    in_memory_repo.add_review(review)

    assert review in in_memory_repo.get_reviews()


def test_repository_does_not_add_a_review_without_a_user(in_memory_repo):
    movie = in_memory_repo.get_movie(2)
    review = Review(None, movie, "i like this movie :)")

    with pytest.raises(RepositoryException):
        in_memory_repo.add_review(review)


def test_repository_does_not_add_a_review_without_a_movie_properly_attached(in_memory_repo):
    user = User('Nina', '123456789')
    in_memory_repo.add_user(user)
    user = in_memory_repo.get_user('Nina')
    movie = in_memory_repo.get_movie(2)
    review = Review(None, movie, "i like this movie :)")

    user.add_review(review)

    with pytest.raises(RepositoryException):
        # Exception expected because the Article doesn't refer to the Comment.
        in_memory_repo.add_review(review)


def test_repository_can_retrieve_reviews(in_memory_repo):
    assert len(in_memory_repo.get_reviews()) == 0
    user = User('Nina', '123456789')
    in_memory_repo.add_user(user)
    user = in_memory_repo.get_user('Nina')
    movie = in_memory_repo.get_movie(2)
    review = make_review(review_text="This movie was average", user=user, movie=movie)

    in_memory_repo.add_review(review)
    assert len(in_memory_repo.get_reviews()) == 1


