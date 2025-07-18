class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.value = None

class Trie:
    """Trie-tietorakenne sananhakuun ja täydentämiseen."""

    def __init__(self):
        """Luo tyhjän Trie-puun."""
        self.root = TrieNode()

    def search(self, word):
        x = self.root
        for i in word:
            if i not in x.children:
                return False
            x = x.children[i]
        return x.is_end_of_word


    def insert(self, word):
        x = self.root
        for i in word:
            if i not in x.children:
                x.children[i] = TrieNode()
            x = x.children[i]
        x.is_end_of_word = True
        
    def starts_with(self, key):
        x = self.root
        for i in key:
            if i not in x.children:
                return False
            x = x.children[i]
        return True