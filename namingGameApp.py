from namingGame import NamingGame

import argparse
import configparser
import json
import logging
import random
import string
import time

LOGGER = logging.getLogger("NamingGameApp")
LOGGER.level = logging.DEBUG


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


def processArguments():
    """
    Process and validate command line arguments.
    """
    parser = argparse.ArgumentParser(description="Configure the Naming Game.")
    parser.add_argument(
        "--configFile",
        default="config.ini",
        help="The configuration file (default is config.ini).",
        type=str,
    )
    parser.add_argument(
        "--targetEnv", default="LOCAL", help="Target environment.", type=str
    )
    parser.add_argument("--startup_message", help="Welcome message", type=str)
    args = parser.parse_args()

    return args


def processConfigs(configFile, environment):
    """
    Process the configuration file.
    """
    configs = configparser.ConfigParser()
    configs.read(configFile)
    return configs[environment]


def run():
    """
    Configure the runtime environment and run the naming game.
    """
    logfile = "output.log"
    LOGGER = setupLogging(filename=logfile)
    LOGGER.info("Booting up the Naming Game.  Processing arguments.")

    args = processArguments()
    LOGGER.debug("Read arguments: " + str(args))
    targetEnv = args.targetEnv if args.targetEnv else "LOCAL"

    configs = processConfigs(args.configFile, targetEnv)
    LOGGER.info(configs["startup_message"])

    game = NamingGame(
        numberOfActors=int(configs["number_of_actors"]),
        maxIterations=int(configs["maximum_iterations"]),
    )
    game.play()


if __name__ == "__main__":
    run()
