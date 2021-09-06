import logging
import random

LOGGER = logging.getLogger("NamingGame")
LOGGER.level = logging.INFO


class Actor(object):
    def __init__(self, name, initialVocabulary=list(), newWordFunction=lambda: "empty"):
        self.name = name
        self.vocabulary = initialVocabulary
        self.newWordFunction = newWordFunction

    def __repr__(self):
        return (
            "Actor(name = " + self.name + ", vocabulary = " + str(self.vocabulary) + ")"
        )

    def __str__(self):
        return "(" + self.name + ", vocabulary = " + str(self.vocabulary) + ")"

    def getVocabulary(self):
        return self.vocabulary

    def speakTo(self, listener, wordToSpeak):
        if wordToSpeak not in self.vocabulary:
            LOGGER.info("Word " + wordToSpeak + " not in listener's vocabulary")
            return False
        LOGGER.info("ACTOR " + str(self) + " said " + wordToSpeak)
        isInListenersVocab = listener.hear(wordToSpeak)
        # if word is in hearer's vocabulary, remove all other words from vocabulary
        if isInListenersVocab:
            self.vocabulary = [wordToSpeak]

    def speakRandomlyTo(self, listener):
        LOGGER.debug("Actor " + str(self) + " getting new word")
        if len(self.vocabulary) is 0:
            self.vocabulary.append(self.newWordFunction())
        wordToSpeak = random.choice(self.vocabulary)
        self.speakTo(listener, wordToSpeak)

    def hear(self, wordSpoken):
        LOGGER.debug(str(self) + " heard word " + str(wordSpoken))
        if wordSpoken in self.vocabulary:
            self.vocabulary = [wordSpoken]
            return True
        else:
            self.vocabulary.append(wordSpoken)
            return False

    def getVocabularySize(self):
        return len(self.vocabulary)
