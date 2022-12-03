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
    with open(filename, "w") as theFile:
        theFile.write(dataToWrite)


class NamingGame(object):
    def __init__(
        self, numberOfActors=7, maxIterations=10, wordLength=10, actors=list()
    ):
        LOGGER.debug(
            "Creating new game! Input params: (numOfActors="
            + str(numberOfActors)
            + ", maxIterations="
            + str(maxIterations)
            + ", wordLength="
            + str(wordLength)
            + ", actors="
            + str(actors)
            + ")"
        )
        self.maxIterations = maxIterations
        self.wordLength = wordLength
        if numberOfActors == 0:
            self.actors = list()
        else:
            self.actors = list()
            for i in range(1, numberOfActors + 1):
                self.actors.append(Actor("Actor" + str(i), set(), self.generateNewWord))
        self.globalVocabulary = set()
        LOGGER.debug("CREATED NEW GAME! Game is: " + str(self))

    def __repr__(self):
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

    def statsWriter(self):
        timeOfRun = str(time.time())
        stats = {
            "run-"
            + timeOfRun: [
                {
                    "number of actors": len(self.actors),
                    "max iterations": self.maxIterations,
                },
            ],
            "IterationDataTypes": "[iteration, totalWords, uniqueWords, probabilityOfSuccess]",
            "iterationData": [],
        }
        while True:
            try:
                blah = yield
                stats.get("iterationData").append(blah)
            except Exception:
                LOGGER.error("Can't collect stats")
            else:
                writeToFile("coroutine-stats-" + timeOfRun + ".json", json.dumps(stats))

    def play(self):
        LOGGER.info(
            "Starting naming game with "
            + str(self.actors)
            + " fully connected actors, and will play for "
            + str(self.maxIterations)
            + " iterations."
        )
        iteration = 1
        statsCollector = self.statsWriter()
        next(statsCollector)
        uniqueWords = self.getNumberOfUniqueWords()
        totalWords = self.getNumberOfWords()
        while not self.isGameComplete(
            iteration, totalWords, uniqueWords, len(self.actors)
        ):
            LOGGER.info("Starting iteration " + str(iteration))
            probabilityOfSuccess = (
                self.iterate()
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
        Perform a single iteration:
          1) Choose a speaker
          2) Choose a listener
          3) Choose a word for the speaker to speak to the listener
          4) Update vocabularies accordingly
        """
        # Randomly choose speaker
        speaker = random.choice(self.actors)
        # Remove listener from actors list before randomly choosing listener
        self.actors.remove(speaker)
        listener = random.choice(self.actors)
        self.actors.append(speaker)
        speaker.speakRandomlyTo(listener)
        LOGGER.info(
            "    SPEAKER " + str(speaker) + " vocab is " + str(speaker.getVocabulary())
        )
        LOGGER.info(
            "    LISTENER "
            + str(listener)
            + " vocab is "
            + str(listener.getVocabulary())
        )
        successfulWords = len(
            speaker.getVocabulary().intersection(listener.getVocabulary())
        )
        probabilityOfSuccess = (
            successfulWords / speaker.getVocabularySize()
        )  # NOT CORRECT
        return probabilityOfSuccess

    def getNumberOfWords(self):
        totalWords = 0
        for actor in self.actors:
            totalWords = totalWords + actor.getVocabularySize()
        return totalWords

    def getNumberOfUniqueWords(self):
        uniqueWords = set()
        for actor in self.actors:
            if len(actor.getVocabulary()) != 0:
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
