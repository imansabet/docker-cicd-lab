from app.main import Movie


def test_movie_requires_title_and_year():
    m = Movie(title="Inception", year=2010, rating=8.8)
    assert m.title == "Inception"
    assert m.year == 2010


def test_movie_rating_optional():
    m = Movie(title="Unknown Film", year=1999)
    assert m.rating is None
