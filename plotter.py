import sys
import logging
import argparse
import configparser
import json
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def getDataFromFile(filename):
    """
    Read data from file to use in plotting.
    """

    with open(filename, "r") as dataFile:
        jsondata = json.load(dataFile)
        actors = jsondata.get('runParams').get('number of actors')
        iterations = jsondata.get('runParams').get('max iterations')
        totalWordsPerIteration = [x[1] for x in jsondata.get('iterationData')]
        uniqueWordsPerIteration = [x[2] for x in jsondata.get('iterationData')]

    return actors, iterations, totalWordsPerIteration, uniqueWordsPerIteration


def generatePlots(filename='', showPlots=True):
    """
    Generate plots for total words and unique words.
    """

    actors, iterations, totalWordsData, uniqueWordsData = getDataFromFile(filename)

    fig1, ax1 = plt.subplots()
    ax1.plot(totalWordsData)
    ax1.set(xlabel='Iteration', ylabel='Total Words', title=f"Naming Game: Known Words (actors {actors}, games {iterations})")
    fig1.savefig('NamingGameTotalWords-' + filename + '.png')

    fig2, ax2 = plt.subplots()
    ax2.plot(uniqueWordsData)
    ax2.set(xlabel='Iteration', ylabel='Unique Words', title=f"Naming Game: Unique Words (actors {actors}, games {iterations})")
    fig2.savefig('NamingGameUniqueWords-' + filename + '.png')
    if showPlots:
        plt.show()
