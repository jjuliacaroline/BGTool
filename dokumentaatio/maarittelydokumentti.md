# Määrittelydokumentti: Kirjoitusvirheiden korjaaja Pythonilla

## Käytettävä ohjelmointikieli
- **Python** 

### Muut hallitsemani kielet

## Toteutetut algoritmit ja tietorakenteet

### Trie

- Sanat tallennetaan trie-tietorakenteeseen, joka mahdollistaa nopean sanahaun ja sanalistauksen.
- Trie mahdollistaa sanan merkkien tehokkaan hakemisen ja terminointitietojen tallennuksen.

### Damerau-Levenshtein -etäisyys

- Algoritmi mittaa kahden merkkijonon "muokkausetäisyyttä" eli tarvittavien lisäysten, poistojen, korvausten ja vierekkäisten merkkien vaihtojen määrää.
- Etäisyys kertoo, kuinka lähellä väärin kirjoitettu sana on oikeaa sanaa.
- Algoritmi toteutetaan matriisipohjaisesti dynaamisella ohjelmoinnilla.

## Ratkaistava ongelma

Ohjelman tavoitteena on tarjota käyttäjälle ehdotuksia oikeinkirjoituksiksi, kun tämä syöttää väärin kirjoitetun sanan.

## Ohjelman syötteet ja niiden käyttö

- **Syötteet:** Käyttäjän kirjoittamat sanat interaktiivisessa tilassa tai erillinen sanalista tiedostosta.
- Korjaaja hakee ehdotukset vertaamalla sanan etäisyyttä sanakirjassa oleviin sanoihin.

## Aika- ja tilavaativuudet

### Trie

- **Aikavaativuus sanan lisäämiselle:** O(n) missä n = sanan pituus.
- **Haun aikavaativuus:** O(n).

### Damerau-Levenshtein-etäisyys

- **Aikavaativuus:** O(m * n), missä m ja n ovat vertailtavien sanojen pituudet.

## Lähteet

- Damerau-Levenshtein-etäisyys:  
  [Geeks for Geeks - Damerau-Levenshtein Distance](https://www.geeksforgeeks.org/damerau-levenshtein-distance/)
  [Damerau–Levenshtein distance](https://en.wikipedia.org/wiki/Damerau–Levenshtein_distance)
- Trie-tietorakenne:  
  [Wikipedia - Trie](https://fi.wikipedia.org/wiki/Trie)
