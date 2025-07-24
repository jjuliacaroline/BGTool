import unittest
from src.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        #Alustetaan Trie ja lisätään muutama sana testejä varten
        self.trie = Trie()
        self.trie.insert("kissa")
        self.trie.insert("koira")
        self.trie.insert("kana")

    def test_insert_and_search_word(self):
        self.assertTrue(self.trie.search("kissa"))

    def test_search_nonexistent_word(self):
        self.assertFalse(self.trie.search("hevonen"))

    def test_partial_word_not_found(self):
        self.assertFalse(self.trie.search("kis"))

    def test_prefix_exists(self):
        self.assertTrue(self.trie.starts_with("ko"))

    def test_prefix_does_not_exist(self):
        self.assertFalse(self.trie.starts_with("hi"))

    def test_empty_prefix_returns_true(self):
        self.assertTrue(self.trie.starts_with(""))

    def test_insert_new_word(self):
        self.trie.insert("poni")
        self.assertTrue(self.trie.search("poni"))
