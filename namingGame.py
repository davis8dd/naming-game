from actor import Actor

import argparse
import configparser
import json
import logging
import random
import string
import time

LOGGER = logging.getLogger("NamingGameApp")
LOGGER.level = logging.DEBUG


def writeToFile(filename, dataToWrite):
    """
    Write data to a specified file.
    """
    with open(filename, "w") as outputFile:
        outputFile.write(dataToWrite)


class NamingGame(object):
    """
    Simulate the Simple Naming Game.
    Initialize the game parameters, perform the simulation, and generate game statistics.
    """

    def __init__(
        self,
        numberOfActors=7,
        maxIterations=10,
        wordLength=10,
        actors=list(),
        gameId="run-" + str(time.time()),
    ):
        """
        Initialize a Naming Game with game parameters.
        """
        LOGGER.info(
            "Creating new game! Input params: (numOfActors="
            + str(numberOfActors)
            + ", maxIterations="
            + str(maxIterations)
            + ", wordLength="
            + str(wordLength)
            + ", actors="
            + str(actors)
            + ", gameId="
            + str(gameId)
            + ")"
        )
        self.maxIterations = maxIterations
        self.wordLength = wordLength
        self.stats = ""
        self.gameId = gameId
        if numberOfActors == 0:
            self.actors = list()
        else:
            self.actors = list()
            for i in range(1, numberOfActors + 1):
                self.actors.append(Actor("Actor" + str(i), set(), self.generateNewWord))
        self.globalVocabulary = set()
        LOGGER.debug("Created game: " + str(self))

    def __str__(self):
        return (
            "NamingGame(numberOfActors="
            + str(len(self.actors))
            + ", maxIterations="
            + str(self.maxIterations)
            + ", wordLength="
            + str(self.wordLength)
            + ", actors="
            + str(self.actors)
            + ", globalVocabulary="
            + str(self.globalVocabulary)
            + ")"
        )

    def __repr__(self):
        return __str__(self)

    def statsWriter(self, stats_id):
        """
        A game statistics map that is written to a JSON file.
        """
        self.stats = {
            "runParams": {
                "id": "run-" + stats_id,
                "number of actors": len(self.actors),
                "max iterations": self.maxIterations,
            },
            "IterationDataTypes": "[iteration, totalWords, uniqueWords, probabilityOfSuccess]",
            "iterationData": [],
        }
        while True:
            try:
                getStats = yield
                self.stats.get("iterationData").append(getStats)
            except Exception:
                LOGGER.error("The statsWriter cannot collect statistics!")
            else:
                LOGGER.debug(f"Stats are {self.stats}")
                writeToFile(self.gameId + ".json", json.dumps(self.stats))

    def play(self):
        """
        Run the naming game.
        """
        LOGGER.debug(
            "Starting naming game for maximum  "
            + str(self.maxIterations)
            + " iterations with the following actors: "
            + str(self.actors)
        )
        LOGGER.info(
            "Starting naming game with "
            + str(len(self.actors))
            + " fully connected actors, and will play for "
            + str(self.maxIterations)
            + " iterations."
        )
        iteration = 1
        statsCollector = self.statsWriter(self.gameId)
        next(statsCollector)
        uniqueWords = self.getNumberOfUniqueWords()
        totalWords = self.getNumberOfWords()
        LOGGER.info(
            "Starting naming game, will stop after "
            + str(self.maxIterations)
            + " iterations."
        )
        while not self._isGameComplete(
            iteration, totalWords, uniqueWords, len(self.actors)
        ):
            LOGGER.debug("Starting iteration " + str(iteration))
            probabilityOfSuccess = (
                self._iterate()
            )  # If all selections are random, what's the ratio of speaker's vocab in listener's vocab?
            uniqueWords = self.getNumberOfUniqueWords()
            totalWords = self.getNumberOfWords()

            statsCollector.send(
                [iteration, totalWords, uniqueWords, probabilityOfSuccess]
            )
            LOGGER.debug("After iteration " + str(iteration) + ", the game state is:")

            for actor in self.actors:
                LOGGER.debug("    " + str(actor))
            iteration += 1
        LOGGER.info(
            "Completed the naming game after " + str(iteration) + " iterations."
        )

    def _isGameComplete(self, iteration, totalWords, uniqueWords, numberOfActors):
        """
        Determine if the naming game is over.
        The game is over when all actors know the same single word.
        The game will also end if the number of rounds played equals the configured limit.
        """
        if iteration > self.maxIterations:
            return True
        if uniqueWords == 1 and totalWords == numberOfActors:
            return True
        return False

    def getActors(self):
        """
        Get all actors.
        """
        return self.actors

    def appendActor(self, anActor):
        """
        Add a new actor.
        """
        self.actors.append(anActor)

    def _iterate(self):
        """
        Perform a single iteration (i.e. game) of the naming game.
        An iteration consists of:
          1) Choosing a speaker
          2) Choosing a listener to be spoken to
          3) Choosing a word for the speaker to speak to the listener
          4) Updating the two actors' vocabularies
        The game is 'successful' if the speaker speaks a word that is
        in the listener's vocabulary.
        """
        speaker = random.choice(self.actors)
        self.actors.remove(speaker)
        listener = random.choice(self.actors)
        self.actors.append(speaker)
        speaker.speakRandomlyTo(listener)
        LOGGER.debug(
            "    SPEAKER " + str(speaker) + " vocab is " + str(speaker.getVocabulary())
        )
        LOGGER.debug(
            "    LISTENER "
            + str(listener)
            + " vocab is "
            + str(listener.getVocabulary())
        )
        successfulWords = len(
            speaker.getVocabulary().intersection(listener.getVocabulary())
        )
        probabilityOfSuccess = (
            # Word from speaker's vocabulary chosen at random
            speaker.getVocabularySize()
            / listener.getVocabularySize()
        )
        return probabilityOfSuccess

    def getNumberOfWords(self):
        """
        Get the total number of words known in all actors' vocabularies.
        A word known by multiple actors will be counted that many times.
        """
        totalWords = 0
        for actor in self.actors:
            totalWords = totalWords + actor.getVocabularySize()
        return totalWords

    def getNumberOfUniqueWords(self):
        """
        Get the number of unique words known in all actors' vocabularies.
        """
        uniqueWords = set()
        for actor in self.actors:
            if len(actor.getVocabulary()) != 0:
                for word in actor.getVocabulary():
                    uniqueWords.add(word)
        return len(uniqueWords)

    def generateNewWord(self):
        """
        Create a new word for actors to communicate.
        The word will be added to the global vocabulary.
        """
        newWord = self._createRandomString(self.wordLength)
        LOGGER.debug("Generated word " + newWord)
        while newWord in self.globalVocabulary:
            newWord = self._createRandomString(self.wordLength)
        self.globalVocabulary.add(newWord)
        LOGGER.debug("Adding new word " + newWord + " to global vocab list")
        return newWord

    def _createRandomString(self, stringLength):
        """
        Return a random string with the given length.
        """
        return "".join(
            random.choice(string.ascii_uppercase) for i in range(stringLength)
        )
