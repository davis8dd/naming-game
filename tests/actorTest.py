from actor import Actor

import unittest

class TestNamingGame(unittest.TestCase):

    def test_empty_initial_vocabulary(self):
        actor1 = Actor("TestActor")
        self.assertTrue(actor1.vocabulary == [])

        actor2 = Actor("Actor2", ["one", "two"])
        self.assertTrue(actor2.vocabulary == ["one", "two"])

    """
    def test_speak_single_word_to_listener(self):
        speaker = Actor(["asdf"])
        listener = Actor()

        print("Speaker vocab is " + str(speaker.getVocabulary()))
        speaker.speakTo(listener=listener, wordToSpeak = "hi")
        print("Listener vocab is " + str(listener.getVocabulary()))

        self.assertTrue(speaker.getVocabulary() == listener.getVocabulary())
    """

    def test_naming_game_failure(self):
        speakerVocab = ["ATSALLAD", "AKNORAB", "AVLA"]
        listenerVocab = ["TARRAB", "AVLA", "OTEROL"]
        listenerVocabAfter = ["TARRAB", "AVLA", "OTEROL", "ATSALLAD"]

        print("Testing failed naming game iteration")
        speaker = Actor(speakerVocab)
        listener = Actor(listenerVocab)
        print("Before speaking:")
        print("Speaker vocab is " + str(speaker.getVocabulary()))
        print("Listener vocab is " + str(listener.getVocabulary()))
        speaker.speakTo(listener=listener, wordToSpeak="ATSALLAD")
        print("After speaking:")
        print("Speaker vocab is " + str(speaker.getVocabulary()))
        print("Listener vocab is " + str(listener.getVocabulary()))
        self.assertTrue(listener.getVocabulary() == listenerVocabAfter)

    def test_naming_game_success(self):
        speakerVocab = ["ATSALLAD", "AKNORAB", "AVLA"]
        listenerVocab = ["TARRAB", "AVLA", "OTEROL"]
        vocabAfter = ["AVLA"]

        print("Testing successful naming game iteration")
        speaker = Actor(speakerVocab)
        listener = Actor(listenerVocab)
        print("Before speaking:")
        print("Speaker vocab is " + str(speaker.getVocabulary()))
        print("Listener vocab is " + str(listener.getVocabulary()))
        speaker.speakTo(listener=listener, wordToSpeak="AVLA")
        print("After speaking:")
        print("Speaker vocab is " + str(speaker.getVocabulary()))
        print("Listener vocab is " + str(listener.getVocabulary()))
        self.assertTrue(listener.getVocabulary() == vocabAfter)
        self.assertTrue(speaker.getVocabulary() == vocabAfter)

    def test_get_vocabulary_size(self):
        speakerVocab = ["ATSALLAD", "AKNORAB", "AVLA"]
        speaker = Actor("speaker", speakerVocab)

        self.assertEqual(speaker.getVocabularySize(), 3)


if __name__ == '__main__':
    unittest.main()
