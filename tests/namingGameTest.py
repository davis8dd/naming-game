from actor import Actor
from namingGame import NamingGame

import unittest


class TestNamingGame(unittest.TestCase):
    def test_getNumberOfWords(self):
        actor1 = Actor("Actor50", initialVocabulary=set(["one", "two"]))
        actor2 = Actor("Actor51", initialVocabulary=set(["one", "three", "four"]))
        game = NamingGame(numberOfActors=0)
        game.appendActor(actor1)
        game.appendActor(actor2)

        self.assertEqual(game.getNumberOfWords(), 5)
        self.assertEqual(game.getNumberOfUniqueWords(), 4)

    def test_game_iteration(self):
        actor1 = Actor("Actor1", initialVocabulary=set(["one"]))
        actor2 = Actor("Actor2", initialVocabulary=set(["two"]))
        game = NamingGame(numberOfActors=0)
        game.appendActor(actor1)
        game.appendActor(actor2)

        game._iterate()

        self.assertEqual(0, 0)

    def test_playSingleIteration(self):
        game = NamingGame(maxIterations=1, numberOfActors=0)
        actor1 = Actor("Actor1", initialVocabulary=set(["one"]))
        actor2 = Actor("Actor2", initialVocabulary=set(["two"]))

        game.appendActor(actor1)
        game.appendActor(actor2)

        game._iterate()

        self.assertEqual(game.getNumberOfWords(), 3)
        self.assertEqual(game.getNumberOfUniqueWords(), 2)

    def test_playSingleIterationWithRandomWord(self):
        game = NamingGame(maxIterations=1, numberOfActors=0)
        actor1 = Actor(
            name="Actor1",
            initialVocabulary=set(),
            newWordFunction=game.generateNewWord,
        )
        actor2 = Actor(
            name="Actor2",
            initialVocabulary=set(),
            newWordFunction=game.generateNewWord,
        )

        game.appendActor(actor1)
        game.appendActor(actor2)

        game._iterate()

        self.assertEqual(game.getNumberOfWords(), 2)
        self.assertEqual(game.getNumberOfUniqueWords(), 1)


    def test_statsWriter(self):
        game = NamingGame(maxIterations=1, numberOfActors=0, gameId="testgame")
        actor1 = Actor(
            name="Actor1",
            initialVocabulary=set(),
            newWordFunction=game.generateNewWord,
        )
        actor2 = Actor(
            name="Actor2",
            initialVocabulary=set(),
            newWordFunction=game.generateNewWord,
        )

        game.appendActor(actor1)
        game.appendActor(actor2)

        game.play()
        print("Game is "+ str(game.stats))

        self.assertEqual(game.stats["run-testgame"], [{'number of actors': 2, 'max iterations': 1}])

if __name__ == "__main__":
    unittest.main()
