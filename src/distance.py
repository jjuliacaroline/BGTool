def damerau_levenshtein(a, b):
    """ Laskee Damerau-Levenshtein-etäisyyden kahden merkkijonon välillä. """
    da = {}
    chars = set(a + b)
    for i in chars:
        da[i] = 0
    
    len1 = len(a)
    len2 = len(b)
    maxdist = len1 + len2
    
    # Luodaan taulukko
    d = [[0] * (len2 + 2) for i in range(len1 + 2)]
    d[0][0] = maxdist
    
    for i in range(len1 + 1):
        d[i + 1][0] = maxdist
        d[i + 1][1] = i
    
    for j in range(len2 + 1):
        d[0][j + 1] = maxdist
        d[1][j + 1] = j
    
    # Lasketaan etäisyydet
    for i in range(1, len1 + 1):
        db = 0
        for j in range(1, len2 + 1):
            i1 = da.get(b[j - 1], 0)
            j1 = db
            
            if a[i - 1] == b[j - 1]:
                cost = 0
                db = j
            else:
                cost = 1
            
            d[i + 1][j + 1] = min(
                d[i][j] + cost,           # substitution
                d[i + 1][j] + 1,          # insertion
                d[i][j + 1] + 1,          # deletion
                d[i1][j1] + (i - i1 - 1) + 1 + (j - j1 - 1) # transposition
            )
        
        # Päivitetään viimeisimmän merkin indeksi
        da[a[i - 1]] = i
    
    return d[len1 + 1][len2 + 1]