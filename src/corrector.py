from src.distance import damerau_levenshtein

def get_words(node, prefix=""):
    """Kerää kaikki sanat trie-rakenteesta."""
    words = []
    if node.is_end_of_word:
        words.append(prefix)
    for char, child in node.children.items():
        words.extend(get_words(child, prefix + char))
    return words

def suggest_correction(trie, word, max_suggestions=3):
    """Ehdottaa korjauksia annetulle sanalle."""
    word_distances = []
    result = []
    all_words = get_words(trie.root)
    if not word.strip():
        return []
    for i in all_words:
        distance = damerau_levenshtein(word, i)
        word_distances.append((i, distance))

    word_distances.sort(key=lambda x: x[1])
    for pair in word_distances[:max_suggestions]:
        w = pair[0]
        result.append(w)
    return result