import logging
import random

LOGGER = logging.getLogger("NamingGame")
LOGGER.level = logging.DEBUG


class Actor(object):
    """
    Actor that participates in the Naming Game.
    This actor has infinite memory.
    """

    def __init__(self, name, initialVocabulary=set(), newWordFunction=lambda: "empty"):
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
        """
        Get the words the actor knows.
        """
        return self.vocabulary

    def speakTo(self, listener, wordToSpeak):
        """
        Speak a specific word to an actor.
        """
        if wordToSpeak not in self.vocabulary:
            LOGGER.info("Word " + wordToSpeak + " not in listener's vocabulary")
            return False
        LOGGER.info("ACTOR " + str(self) + " said " + wordToSpeak)
        isInListenersVocab = listener.hear(wordToSpeak)
        # if word is in hearer's vocabulary, remove all other words from vocabulary
        if isInListenersVocab:
            self.vocabulary.clear()
            self.vocabulary.add(wordToSpeak)

    def speakRandomlyTo(self, listener):
        """
        Speak a random word to an actor.
        """
        LOGGER.debug("Actor " + str(self) + " getting new word")
        if len(self.vocabulary) == 0:
            self.vocabulary.add(self.newWordFunction())
        wordToSpeak = random.choice(list(self.vocabulary))
        self.speakTo(listener, wordToSpeak)

    def hear(self, wordSpoken):
        """
        Hear a word.  If the word is already known, then forget all other words.
        If the word is not known, add it to the existing vocabulary.
        """
        LOGGER.debug(str(self) + " heard word " + str(wordSpoken))
        if wordSpoken in self.vocabulary:
            self.vocabulary.clear()
            self.vocabulary.add(wordSpoken)
            return True
        else:
            self.vocabulary.add(wordSpoken)
            return False

    def getVocabularySize(self):
        """
        Get the number of words the actor knows.
        """
        return len(self.vocabulary)
