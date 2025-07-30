# Testausdokumentti
## Yksikkötestauksen kattavuusraportti

Projektin yksikkötestaus kattaa neljä päämoduulia:
- **Trie-tietorakenne** (`test_trie.py`): 9 testiä
- **Damerau-Levenshtein etäisyysalgoritmi** (`test_distance.py`): 6 testiä  
- **Korjausehdotusten generointialgorimi** (`test_corrector.py`): 4 testiä
- **Integraatiotestit** (`test_integration.py`): 2 testiä
**Yhteensä 21 yksikkötestiä** kattavat järjestelmän kaikki keskeiset toiminnallisuudet.

## Mitä on testattu ja miten

### Trie-tietorakenne testaus
Trie-tietorakenteen testaus keskittyi varmistamaan perusoperaatioiden toimivuus:

- **Sanojen lisääminen ja hakeminen**: Testattu, että Trie-rakenteeseen lisätyt sanat "kissa", "koira" ja "kana" löytyvät hakuoperaatiolla
- **Olemattomien sanojen haku**: Varmistettu, että sanaa "hevonen" ei löydy rakenteesta
- **Osittaisten hakujen käsittely**: Testattu, että pelkkä etuliite "kis" ei palaudu kokonaisena sanana
- **Etuliitteiden tunnistaminen**: Varmistettu, että `starts_with("ko")` palauttaa `True` (löytyy "koira")
- **Tyhjän etuliitteen käsittely**: Testattu, että tyhjä merkkijono palauttaa `True` etuliitehaussa
- **Iteraatio**: Varmistettu, että Trie-rakenne tukee for-silmukalla iterointia ja palauttaa kaikki tallennetut sanat

### Damerau-Levenshtein etäisyysalgoritmin testaus
Etäisyysalgoritmin testaus kattoi kaikki mahdolliset merkkijonomuutokset:

- **Identtiset merkkijonot**: Testattu, että "kissa" ja "kissa" antavat etäisyyden 0
- **Lisäysoperaatio**: Varmistettu, että "kissa" → "kissaa" antaa etäisyyden 1
- **Poistooperaatio**: Testattu, että "kissa" → "kisa" antaa etäisyyden 1  
- **Korvausoperaatio**: Varmistettu kahdella eri parilla: "kissa" → "kassa" (etäisyys 1) ja "talo" → "palo" (etäisyys 1)
- **Transpositio (merkkien vaihto)**: Testattu "kisa" → "kasi" (etäisyys 2) ja "kasi" → "ksai" (etäisyys 1)
- **Tyhjät merkkijonot**: Varmistettu, että tyhjien merkkijonojen etäisyys on 0 ja "kissa" → "" antaa etäisyyden 5

### Korjausehdotusten generointialgorimin testaus
Pääalgoritmin testaus keskittyi käytännön toimivuuteen:

- **Ehdotusten määrän rajoittaminen**: Testattu, että `max_suggestions=2` parametrilla palautetaan maksimissaan 2 ehdotusta
- **Tarkan osuman priorisointi**: Varmistettu, että kun haetaan sanaa "kissa" ja se löytyy sanastosta, se palautetaan ensimmäisenä ehdotuksena
- **Lähimpien sanojen löytäminen**: Testattu, että syötteelle "kisi" algoritmi ehdottaa sanaa "kissa"
- **Tyhjän syötteen käsittely**: Varmistettu, että tyhjä merkkijono palauttaa tyhjän ehdotuslistan

### Integraatiotestaus
Integraatiotestit varmistavat komponenttien yhteistoimivuuden:

**Trie-integraatio:** Testattu että insert, search, starts_with ja iteraatio toimivat oikein yhdessä
**Corrector-integraatio:** Varmistettu että korjausehdotusalgoritmi toimii Trie-tietorakenteen kanssa oikein

## Testisyötteet

### Testisanasto
Kaikissa testeissä käytettiin yhtenäistä testisanastoa:
- "kissa" (5 merkkiä)
- "koira" (5 merkkiä)  
- "kasi" (4 merkkiä)
- "koti" (4 merkkiä)
- "kana" (4 merkkiä, vain Trie-testeissä)
- "poni" (4 merkkiä, lisätty dynaamisesti testeissä)

### Testisyötteiden tyypitys
- **Oikeat sanat**: "kissa", "koira" (tarkkuuden testaus)
- **Yhden merkin virheet**: "kisa" (poisto), "kissaa" (lisäys), "kassa" (korvaus)
- **Monitoimiset virheet**: "kisi" (useampi muutos), "kasi" (transposition)
- **Rajatapaukset**: Tyhjä merkkijono, olemattomat sanat
- **Etuliitteet**: "ko", "kis", "hi" (olematon)

## Testien toistaminen

Testit voidaan ajaa seuraavilla komennoilla:

Pytestillä:
```bash
pytest src
```

Unittestillä
```bash
python -m unittest discover -s src/tests
```

Pylintillä
```bash
pylint src
```

Yksittäinen testitiedosto
```bash
python -m unittest src.tests.test_trie
python -m unittest src.tests.test_distance  
python -m unittest src.tests.test_corrector
```
