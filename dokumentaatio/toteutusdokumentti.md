**Ohjelman yleisrakenne**:
Ohjelma rakentuu seuraavista moduuleista:

**trie.py**: Sisältää Trie-tietorakenteen toteutuksen, jota käytetään sanaston tallennukseen ja sanahakuihin.
**distance.py**: Toteuttaa Damerau-Levenshtein-algoritmin, joka huolehtii etäisyyksien laskemisesta.
**corrector.py**: Korjausehdotusalgoritmi, joka hyödyntää Trie-rakennetta sekä etäisyyttä lähimpien oikeinkirjoitettujen sanojen löytämiseksi.
**main.py**: Käyttöliittymä terminaalille, jonka kautta käyttäjä voi syöttää sanoja ja saada korjausehdotuksia.

**Saavutetut aika- ja tilavaativuudet**:
**Trie-tietorakenne**: O(n), missä n on sanan pituus
**Damerau-Levenshtein**:
**Aikavaativuus:** O(n·m), missä n ja m ovat syötteiden pituudet.
**Tilavaativuus:** O(n·m), johtuen matriisin käytöstä välimuistin tallennukseen.

**Suorituskyky- ja O-analyysivertailu**:
- Trie-tietorakenne mahdollistaa merkittävästi nopeamman hakemisen kuin lineaarinen sanaston läpikäynti.
- Damerau-Levenshtein toimii hyvin lyhyillä sanoilla, mutta suorituskyky heikkenee pitemmillä sanoilla ja suuremmilla sanastoilla.

**Työn mahdolliset puutteet ja parannusehdotukset**:
- Suurilla sanastoilla ja pitkällä syötteellä suorituskyky voi heikentyä

**Laajojen kielimallien (ChatGPT yms.) käyttö.**:
Tässä projektissa on käytetty OpenAI:n ChatGPT-mallia avustamaan seuraavissa tehtävissä:
- Testausdokumentin ja viikkoraporttien muotoilussa.
- Määrittelydokumentin ja toteutusdokumentin muotoilussa.
- Testitapausten ideoinnin tukena.

**Lähteet, joita olet käyttänyt**:
[Trie-algoritmi](https://en.wikipedia.org/wiki/Trie)
[Damerau-Levenshtein-algoritmi](https://en.wikipedia.org/wiki/Damerau–Levenshtein_distance)
[Trie Data Structure](https://www.geeksforgeeks.org/dsa/trie-insert-and-search/)