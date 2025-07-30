class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    """Trie-tietorakenne sananhakuun ja täydentämiseen."""

    def __init__(self):
        """Luo tyhjän Trie-puun."""
        self.root = TrieNode()

    def __str__(self):
        """Palauttaa kaikki Trieen tallennetut sanat syvyyshaun mukaisessa järjestyksessä."""
        return ', '.join(self._collect_words())
    
    def __iter__(self):
        """Mahdollistaa Trieen tallennettujen sanojen läpikäynnin for-silmukalla."""
        return iter(self._iterate(self.root, ""))
    
    def _collect_words(self, node=None, prefix='', words=None):
        if words is None:
            words = []
        if node is None:
            node = self.root

        if node.is_end_of_word:
            words.append(prefix)

        for i in sorted(node.children.keys()):
            self._collect_words(node.children[i], prefix + i, words)

        return words

    def _iterate(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for i in sorted(node.children):
            words.extend(self._iterate(node.children[i], prefix + i))
        return words

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