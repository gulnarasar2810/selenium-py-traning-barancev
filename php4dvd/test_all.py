# -*- coding: utf-8 -*- #
from model.user import User
#from selenium_fixture import app


def test_with_valid_credentials(app):
    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.logout()
    assert app.is_not_logged_in()

def test_with_invalid_credentials(app):
    app.ensure_logout()
    app.login(User.random())
    assert app.is_not_logged_in()










