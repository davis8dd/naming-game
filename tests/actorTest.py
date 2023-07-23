from actor import Actor

import unittest


class TestNamingGame(unittest.TestCase):
    """
    Test the NamingGame API.
    """

    def test_empty_initial_vocabulary(self):
        """
        Test initializing actor's vocabulary with an empty set and also with a non-empty set.
        """
        actor1 = Actor("TestActor")
        self.assertTrue(actor1.vocabulary == set())

        actor2 = Actor("Actor2", set(["one", "two"]))
        self.assertTrue(actor2.vocabulary == set(["one", "two"]))

    def test_naming_game_failure(self):
        """
        Validate listener gains vocabulary after listening to a new word.
        """
        speakerVocab = ["ATSALLAD", "AKNORAB", "AVLA"]
        listenerVocab = ["TARRAB", "AVLA", "OTEROL"]
        listenerVocabAfter = ["TARRAB", "AVLA", "OTEROL", "ATSALLAD"]

        speaker = Actor("speaker", set(speakerVocab))
        listener = Actor("listener", set(listenerVocab))
        speaker.speakTo(listener=listener, wordToSpeak="ATSALLAD")
        self.assertEqual(listener.getVocabulary(), set(listenerVocabAfter))

    def test_naming_game_success(self):
        """
        Validate listener and speaker vocabularies collapse after listening to a known word.
        """
        speakerVocab = ["ATSALLAD", "AKNORAB", "AVLA"]
        listenerVocab = ["TARRAB", "AVLA", "OTEROL"]
        vocabAfter = ["AVLA"]

        speaker = Actor("speaker", set(speakerVocab))
        listener = Actor("listener", set(listenerVocab))
        speaker.speakTo(listener=listener, wordToSpeak="AVLA")
        self.assertEqual(listener.getVocabulary(), set(vocabAfter))
        self.assertEqual(speaker.getVocabulary(), set(vocabAfter))

    def test_get_vocabulary_size(self):
        """
        Validate getVocabularySize() matches number of words vocabulary word size.
        """
        speakerVocab = ["ATSALLAD", "AKNORAB", "AVLA"]
        speaker = Actor("speaker", set(speakerVocab))

        self.assertEqual(speaker.getVocabularySize(), 3)


if __name__ == "__main__":
    unittest.main()
