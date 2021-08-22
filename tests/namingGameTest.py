from actor import Actor
from namingGame import NamingGame

import unittest

class TestNamingGame(unittest.TestCase):

    def test_game_iteration(self):
        actor1 = Actor("Actor1", ["one"])
        actor2 = Actor("Actor2", ["two"])
        game = NamingGame()
        game.appendActor(actor1)
        game.appendActor(actor2)
        game.iterate()


if __name__ == '__main__':
    unittest.main()
