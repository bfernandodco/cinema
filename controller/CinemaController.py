from model.Filme import Filme
from model.Serie import Serie


class CinemaController:
    mr_robot = Serie('mr_robot', 2015, 4)
    mr_robot.dar_likes(14)
    breaking_bad = Serie('breaking bad', 2008, 5)

    vingadores = Filme('vingadores - guerra infinita', 2018, 160)
    vingadores.dar_likes(7)
    harry_potter = Filme('harry potter - pedra filosofal', 2001, 140)
    harry_potter.dar_likes(7)

    filme_series = [mr_robot, breaking_bad, vingadores, harry_potter]
    for imprime in filme_series:
        imprime.imprime()