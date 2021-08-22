import random

class Actor(object):
    def __init__(self, name, initialVocabulary = list()):
        self.name = name
        self.vocabulary = initialVocabulary

    def __repr__(self):
        return "Actor(name = " + self.name + ", vocabulary = " + str(self.vocabulary) + ")"

    def __str__(self):
        return "(" + self.name + ", vocabulary = " + str(self.vocabulary) + ")"

    def getVocabulary(self):
        return self.vocabulary

    def speakTo(self, listener, wordToSpeak):
        if wordToSpeak not in self.vocabulary:
            print("Word " + wordToSpeak + " not in listener's vocabulary")
            return False
        print(str(self) + " said " + wordToSpeak)
        isInListenersVocab = listener.hear(wordToSpeak)
        # if word is in hearer's vocabulary, remove all other words from vocabulary
        if isInListenersVocab:
            self.vocabulary = [wordToSpeak]

    def speakRandomlyTo(self, listener):
        wordToSpeak = random.choice(self.vocabulary)
        self.speakTo(listener, wordToSpeak)

    def hear(self, wordSpoken):
        print(str(self) + " heard word " + str(wordSpoken))
        if wordSpoken in self.vocabulary:
            self.vocabulary = [wordSpoken]
            return True
        else:
            self.vocabulary.append(wordSpoken)
            return False

    def get_random_word(self, wordList):
        """
        Get a new word from the allowed list and add it to the vocabulary.
        TODO: THIS LIST SHOULD BE COMING FROM THE GAME OBJECT.
        """
        newWord = random.choice(wordList)
        return newWord
