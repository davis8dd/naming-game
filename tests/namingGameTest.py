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

    def test_getNumberOfWords(self):
        actor1 = Actor("Actor1", ["one", "two"])
        actor2 = Actor("Actor2", ["one", "three", "four"])
        game = NamingGame()
        game.appendActor(actor1)
        game.appendActor(actor2)

        self.assertEqual(game.getNumberOfWords(), 5)
        self.assertEqual(game.getNumberOfUniqueWords(), 4)


if __name__ == "__main__":
    unittest.main()
