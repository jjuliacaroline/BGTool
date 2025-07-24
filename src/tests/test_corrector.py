import unittest
from src.corrector import suggest_correction
from src.trie import Trie

class TestCorrector(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        words = ["kissa", "koira", "kasi", "koti"]
        for word in words:
            self.trie.insert(word)

    def test_suggestions_limit(self):
        suggestions = suggest_correction(self.trie, "kisa", max_suggestions=2)
        self.assertLessEqual(len(suggestions), 2)

    def test_exact_match_first(self):
        suggestions = suggest_correction(self.trie, "kissa")
        self.assertEqual(suggestions[0], "kissa")

    def test_suggestions_close_words(self):
        suggestions = suggest_correction(self.trie, "kisi")
        self.assertIn("kissa", suggestions)

    def test_empty_input(self):
        suggestions = suggest_correction(self.trie, "")
        self.assertEqual(suggestions, [])
