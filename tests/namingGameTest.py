from actor import Actor
from namingGame import NamingGame

import unittest


class TestNamingGame(unittest.TestCase):

    def test_getNumberOfWords(self):
        actor1 = Actor("Actor50", initialVocabulary=["one", "two"])
        actor2 = Actor("Actor51", initialVocabulary=["one", "three", "four"])
        game = NamingGame(numberOfActors=0)
        game.appendActor(actor1)
        game.appendActor(actor2)

        self.assertEqual(game.getNumberOfWords(), 5)
        self.assertEqual(game.getNumberOfUniqueWords(), 4)

    def test_game_iteration(self):
        actor1 = Actor("Actor1", initialVocabulary=["one"])
        actor2 = Actor("Actor2", initialVocabulary=["two"])
        game = NamingGame(numberOfActors=0)
        game.appendActor(actor1)
        game.appendActor(actor2)

        game.iterate()

        self.assertEqual(0, 0)

    def test_playSingleIteration(self):
        game = NamingGame(maxIterations=1, numberOfActors=0)
        actor1 = Actor("Actor1", initialVocabulary=["one"])
        actor2 = Actor("Actor2", initialVocabulary=["two"])

        game.appendActor(actor1)
        game.appendActor(actor2)

        game.play()

        self.assertEqual(game.getNumberOfWords(), 3)
        self.assertEqual(game.getNumberOfUniqueWords(), 2)

    def test_playSingleIterationWithRandomWord(self):
        game = NamingGame(maxIterations=1, numberOfActors=0)
        actor1 = Actor(name="Actor1", initialVocabulary=list(), newWordFunction=game.generateNewWord)
        actor2 = Actor(name="Actor2", initialVocabulary=list(), newWordFunction=game.generateNewWord)

        game.appendActor(actor1)
        game.appendActor(actor2)

        game.play()

        self.assertEqual(game.getNumberOfWords(), 2)
        self.assertEqual(game.getNumberOfUniqueWords(), 1)


if __name__ == "__main__":
    unittest.main()
