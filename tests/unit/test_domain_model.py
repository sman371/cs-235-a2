from datetime import date

from movies.domain.model1 import Movie, Genre, Director, Actor, Review, make_review, User

import pytest


@pytest.fixture()
def movie():
    return Movie(
        "Guardians of the Galaxy",
        2014
    )


@pytest.fixture()
def user():
    return User('dbowie', '1234567890')


@pytest.fixture()
def actor():
    return Actor('Tina Fey')

@pytest.fixture()
def genre():
    return Genre('Drama')

@pytest.fixture()
def director():
    return Director('Tom Joy')


def test_user_construction(user):
    assert user.username == 'dbowie'
    assert user.password == '1234567890'
    assert repr(user) == '<User dbowie 1234567890>'

    for review in user.reviews:
        # User should have an empty list of reviews after construction.
        assert False


def test_movie_construction(movie):
    assert movie.id is None
    assert movie.year == 2014
    assert movie.title == 'Guardians of the Galaxy'

    assert len(movie.reviews) == 0
    assert len(movie.actors) == 0
    assert len(movie.genres) == 0
    assert movie.director is None

    assert repr(movie) == '<Movie Guardians of the Galaxy, 2014>'


def test_article_less_than_operator(movie):
    movie1 = Movie(
        "Apples",
        None
    )

    movie2 = Movie(
        'Guardians of the Galaxy',
        2020
    )

    assert movie1 < movie
    assert movie < movie2


def test_actor_construction(actor):
    assert actor.actor_full_name == 'Tina Fey'

    for colleague in actor.colleagues:
        assert False


def test_make_review_establishes_relationships(movie, user):
    review_text = 'very bad'
    #rating = 1
    review = make_review(review_text=review_text, user=user, movie=movie)

    # Check that the User object knows about the review.
    assert review in user.reviews

    # Check that the review knows about the User.
    assert review.user is user

    # Check that movie knows about the review.
    assert review in movie.reviews

    # Check that the review knows about the movie.
    assert review.movie is movie


# def test_make_tag_associations(article, tag):
#     make_tag_association(article, tag)
#
#     # Check that the Article knows about the Tag.
#     assert article.is_tagged()
#     assert article.is_tagged_by(tag)
#
#     # check that the Tag knows about the Article.
#     assert tag.is_applied_to(article)
#     assert article in tag.tagged_articles
#
#
# def test_make_tag_associations_with_article_already_tagged(article, tag):
#     make_tag_association(article, tag)
#
#     with pytest.raises(ModelException):
#         make_tag_association(article, tag)
