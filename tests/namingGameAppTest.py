import namingGameApp
import unittest


class TestNamingGame(unittest.TestCase):
    def test_getNumberOfWords(self):
        testConfigFilename = "tests/testNamingGameConfig.ini"
        targetEnvironment = "LOCAL"
        configs = namingGameApp.processConfigs(testConfigFilename, targetEnvironment)


if __name__ == "__main__":
    unittest.main()
