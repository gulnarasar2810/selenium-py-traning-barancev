import random

class User(object):

    def __init__(self, username="", password="", email=""):
        self.username = username
        self.password = password
        self.email = email

    @classmethod
    def Admin(cls):
        return cls(username="admin", password="admin")

    @classmethod
    def random(cls):
        random_nmb = random.randrange(0,10000)
        username_rnd = "admin" + str(random_nmb)
        password_rnd = "admin" + str(random_nmb)
        email_rnd = "admin" + str(random_nmb)+ "@test.test"
        return cls(username=username_rnd, password=password_rnd, email=email_rnd)


