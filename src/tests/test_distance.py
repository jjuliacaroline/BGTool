import unittest
from src.distance import damerau_levenshtein

class TestDistance(unittest.TestCase):
    def test_identical_strings(self):
        self.assertEqual(damerau_levenshtein("kissa", "kissa"), 0)

    def test_insertion(self):
        self.assertEqual(damerau_levenshtein("kissa", "kissaa"), 1)

    def test_deletion(self):
        self.assertEqual(damerau_levenshtein("kissa", "kisa"), 1)

    def test_substitution(self):
        self.assertEqual(damerau_levenshtein("kissa", "kassa"), 1)
        self.assertEqual(damerau_levenshtein("talo", "palo"), 1)

    def test_transposition(self):
        self.assertEqual(damerau_levenshtein("kisa", "kasi"), 2)
        self.assertEqual(damerau_levenshtein("kasi", "ksai"), 1)

    def test_empty_strings(self):
        self.assertEqual(damerau_levenshtein("", ""), 0)
        self.assertEqual(damerau_levenshtein("kissa", ""), 5)
