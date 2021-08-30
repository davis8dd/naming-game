from actor import Actor

import json
import logging
import random
import string
import time

LOGGER = logging.getLogger("NamingGame")
LOGGER.level = logging.INFO


class NamingGame(object):
    def __init__(self, maxIterations=10, wordLength=10):
        self.maxIterations = maxIterations
        self.wordLength = wordLength
        self.actors = list()
        self.globalVocabulary = set()
        LOGGER.info("Starting NamingGame")

    def __repr__(self):
        return (
            "NamingGame(actors="
            + str(self.actors)
            + ", maxIterations="
            + str(self.maxIterations)
            + ")"
        )

    def __str__(self):
        return "A naming game instance with " + str(self.actors) + " actors."

    def play(self):
        LOGGER.info(
            "Starting naming game with "
            + str(self.actors)
            + " fully connected actors, and will play for "
            + str(self.maxIterations)
            + " iterations."
        )
        iteration = 1
        timeOfRun = str(time.time())
        stats = {
            "run-"
            + timeOfRun: [
                {"iterations": self.maxIterations},
            ],
            "iterationData": [],
        }
        uniqueWords = self.getNumberOfUniqueWords()
        totalWords = self.getNumberOfWords()
        while not self.isGameComplete(
            iteration, totalWords, uniqueWords, len(self.actors)
        ):
            LOGGER.info("Starting iteration " + str(iteration))
            self.iterate()
            uniqueWords = self.getNumberOfUniqueWords()
            totalWords = self.getNumberOfWords()
            stats.get("iterationData").append([iteration, totalWords, uniqueWords])
            LOGGER.info("After iteration " + str(iteration) + ", the game state is:")
            for actor in self.actors:
                LOGGER.info("    " + str(actor))
            iteration += 1
        writeToFile("stats-" + timeOfRun + ".json", json.dumps(stats))

    def isGameComplete(self, iteration, totalWords, uniqueWords, numberOfActors):
        if iteration > self.maxIterations:
            return True
        if uniqueWords == 1 and totalWords == numberOfActors:
            return True
        return False

    def getActors(self):
        return self.actors

    def appendActor(self, anActor):
        self.actors.append(anActor)

    def iterate(self):
        """
        Asdf.
        """
        # Randomly choose speaker
        speaker = random.choice(self.actors)
        # Remove listener from actors list before randomly choosing listener
        self.actors.remove(speaker)
        listener = random.choice(self.actors)
        self.actors.append(speaker)
        speaker.speakRandomlyTo(listener)

    def getNumberOfWords(self):
        totalWords = 0
        for actor in self.actors:
            totalWords = totalWords + actor.getVocabularySize()
        return totalWords

    def getNumberOfUniqueWords(self):
        uniqueWords = set()
        for actor in self.actors:
            for word in actor.getVocabulary():
                uniqueWords.add(word)
        return len(uniqueWords)

    def generateNewWord(self):
        newWord = "".join(
            random.choice(string.ascii_uppercase) for i in range(self.wordLength)
        )
        LOGGER.info("Generated word " + newWord)
        while newWord in self.globalVocabulary:
            newWord = "".join(
                random.choice(string.ascii_uppercase) for i in Range(self.wordLength)
            )
        self.globalVocabulary.add(newWord)
        LOGGER.info("Adding new word " + newWord + " to global vocab list")
        return newWord


def setupLogging(filename):
    """
    Initialize logging.  One logger outputs to a file and another outputs to the console.
    """
    fileLogHandler = logging.FileHandler(filename)

    fileLogHandler.setLevel(logging.DEBUG)
    fileFormatter = logging.Formatter(
        "%(asctime)s %(name)-12s %(levelname)-8s %(message)s"
    )
    fileLogHandler.setFormatter(fileFormatter)
    LOGGER.addHandler(fileLogHandler)

    consoleLogHandler = logging.StreamHandler()
    consoleLogHandler.setLevel(logging.INFO)
    LOGGER.addHandler(consoleLogHandler)

    return LOGGER


def writeToFile(filename, dataToWrite):
    with open(filename, "w") as theFile:
        theFile.write(dataToWrite)


if __name__ == "__main__":
    """
    Run the game.
    """
    logfile = "output.log"
    LOGGER = setupLogging(filename=logfile)
    LOGGER.info("Starting game")
    game = NamingGame(15)
    actor1 = Actor("Actor1", list(), game.generateNewWord)
    actor2 = Actor("Actor2", list(), game.generateNewWord)
    actor3 = Actor("Actor3", list(), game.generateNewWord)
    actor4 = Actor("Actor4", list(), game.generateNewWord)
    actor5 = Actor("Actor5", list(), game.generateNewWord)
    game.appendActor(actor1)
    game.appendActor(actor2)
    game.appendActor(actor3)
    game.appendActor(actor4)
    game.appendActor(actor5)
    game.play()
