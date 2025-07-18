import unittest
from src.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        # Alustetaan tyhjä Trie ennen jokaista testiä ja lisätään perussanat
        self.trie = Trie()
        self.trie.insert("kissa")
        self.trie.insert("koira")
        self.trie.insert("kana")

    def test_sanan_lisays_ja_haku(self):
        self.assertTrue(self.trie.search("kissa"))

    def test_sanaa_ei_loydy_jos_ei_lisatty(self):
        self.assertFalse(self.trie.search("hevonen"))

    def test_osittainen_sana_ei_kelpaa(self):
        self.assertFalse(self.trie.search("kis"))

    def test_etuliite_loytyy(self):
        self.assertTrue(self.trie.starts_with("ko"))

    def test_etuliite_ei_loydy(self):
        self.assertFalse(self.trie.starts_with("hi"))

    def test_tyhja_etuliite_palauttaa_true(self):
        self.assertTrue(self.trie.starts_with(""))

    def test_uuden_sanan_lisays_toimii(self):
        self.trie.insert("poni")
        self.assertTrue(self.trie.search("poni"))