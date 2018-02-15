import random

class Movie(object):

    def __init__(self, title="", year="", format="DVD"):
        self.title = title
        self.year = year
        self.format = format

    @classmethod
    def random(cls):
        rnd_number = random.randrange(0, 10000)
        movie_name = "Movie name" + str(rnd_number)
        rnd_year = str(random.randrange(1900, 2017))
        return cls(title=movie_name, year=rnd_year)


