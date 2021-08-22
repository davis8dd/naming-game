from actor import Actor

import logging
import random

LOGGER = logging.getLogger('NamingGame')
LOGGER.level = logging.INFO

class NamingGame(object):
    def __init__(self):
        self.actors = list()
        self.newWords = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        LOGGER.info("Starting NamingGame")

    def __repr__(self):
        return "The internal representation of a NamingGame"

    def __str__(self):
        return "A naming game instance with " + str(self.actors) + " actors."

    def play(self, iterationsToPlay):
        LOGGER.info("Starting naming game with " + str(self.actors)
                + " fully connected actors, and will play for " + str(iterationsToPlay) + " iterations.")
        iteration = 0
        while iteration < iterationsToPlay:
            LOGGER.info("Starting iteration " + str(iteration))
            self.iterate()
            iteration = iteration + 1
            LOGGER.info("After iteration " + str(iteration) + ", the game state is:")
            for actor in self.actors:
                LOGGER.info("    " + str(actor))

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

def setupLogging(filename):
    """
    Initialize logger.
    """
    fileLogHandler = logging.FileHandler(filename)

    fileLogHandler.setLevel(logging.DEBUG)
    fileFormatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
    fileLogHandler.setFormatter(fileFormatter)
    LOGGER.addHandler(fileLogHandler)

    consoleLogHandler = logging.StreamHandler()
    consoleLogHandler.setLevel(logging.INFO)
    LOGGER.addHandler(consoleLogHandler)

    return LOGGER


if __name__ == '__main__':
    """
    Run the game.
    """
    logfile = 'output.log'
    LOGGER = setupLogging(filename=logfile)
    LOGGER.info("Starting game")
    actor1 = Actor("Actor1", ["one"])
    actor2 = Actor("Actor2", ["two"])
    actor3 = Actor("Actor3", ["three"])
    actor4 = Actor("Actor4", ["four"])
    actor5 = Actor("Actor5", ["five"])
    game = NamingGame()
    game.appendActor(actor1)
    game.appendActor(actor2)
    game.appendActor(actor3)
    game.appendActor(actor4)
    game.appendActor(actor5)
    game.play(10)
