from model.user import User
from model.movie import Movie
#from selenium_fixture import app

def test_add_movie(app):
    new_movie = Movie.random()
    app.ensure_login_as(User.Admin())
    app.add_movie(new_movie)
    assert app.is_added_movie(new_movie)

