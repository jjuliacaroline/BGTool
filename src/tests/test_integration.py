import unittest
from src.trie import Trie
from src.corrector import suggest_correction

class TestTrieIntegration(unittest.TestCase):
    def test_integration_trie(self):
        trie = Trie()
        words = ["kissa", "koira", "kana"]

        for i in words:
            trie.insert(i)

        for i in words:
            self.assertTrue(trie.search(i))

        self.assertTrue(trie.starts_with("ki"))
        self.assertTrue(trie.starts_with("ko"))
        self.assertFalse(trie.starts_with("he"))

        iterated_words = set(trie)
        self.assertEqual(iterated_words, set(words))

class TestCorrectorIntegration(unittest.TestCase):
    def test_integration_corrector(self):
        trie = Trie()
        words = ["kissa", "koira", "kasi", "koti"]

        for i in words:
            trie.insert(i)

        # Testataan ehdotukset tarkalle osumalle
        suggestions = suggest_correction(trie, "kissa")
        self.assertEqual(suggestions[0], "kissa")

        # Testataan ehdotukset läheiselle sanalle
        suggestions = suggest_correction(trie, "kasi")
        self.assertIn("kasi", suggestions)
        self.assertIn("kissa", suggestions)

        # Testataan tyhjä syöte
        suggestions = suggest_correction(trie, "")
        self.assertEqual(suggestions, [])

        # Lisätään sana ja tarkastetaan ehdotukset
        trie.insert("kala")
        suggestions = suggest_correction(trie, "kala")
        self.assertIn("kala", suggestions)

if __name__ == "__main__":
    unittest.main()
