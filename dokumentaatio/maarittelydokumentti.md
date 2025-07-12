# Määrittelydokumentti

## Opinto-ohjelma
Tietojenkäsittelytiede

## Projektin kieli
Suomi

## Projektin nimi
BGTool

## Käytettävä ohjelmointikieli
Python

## Muut hallitsemani kielet


## Projektin ydin
Projektin ydin on Pythonilla toteutettava banner grabbing -työkalu, joka yhdistyy määriteltyihin IP-osoitteisiin ja portteihin, ja yrittää tunnistaa niissä toimivat palvelinohjelmistot ja niiden versiot. Tunnistaminen perustuu TCP-protokollan kautta lähetettäviin palveluiden aloitusviesteihin ("bannereihin"), joita monet palvelut kuten HTTP, SSH ja FTP lähettävät heti yhteyden muodostuksen jälkeen.

## Ongelma, jonka ratkaisen
Tämä työkalu tarjoaa yksinkertaisen tavan kartoittaa ja tunnistaa avoinna olevia palveluita ja niiden mahdollisia versioita, mikä voi auttaa mm. tietoturvan hallinnassa ja verkon dokumentoinnissa.

## Käytettävät algoritmit ja tietorakenteet
- TCP-soketit: Pythonin socket-moduulin käyttö suoraan TCP-yhteyksien luomiseen.
- Aikakatkaisujen hallinta.
- Porttiskannaus: Yksinkertaisen lineaarisen porttihaku-algoritmi, jossa skannataan peräkkäin halutut portit kohdeosoitteissa.
- Regex-analyysi: Vastauksista yritetään erottaa palvelinohjelmiston nimi ja versio säännöllisten lausekkeiden avulla.

## Syötteet ja niiden käyttö
- IP-osoitteet ja porttialueet annetaan komentoriviparametreina tai syötetään konfiguraatiotiedostona.
- Tulokset tulostetaan konsoliin ja haluttaessa tallennetaan CSV- tai JSON-tiedostoon.

### Aikavaativuus
- Yhden portin tarkistus yhdelle IP:lle: **O(1)** (vakioaikainen yhteysyritys + vasteen odotus)
- Koko verkon skannaus (n IP:tä, m porttia/IP): **O(n * m)**

### Tilavaativuus
- Vain tulokset tallennetaan: **O(n * m)**, missä `n` on IP-osoitteiden määrä ja `m` porttien määrä.
- Muisti ei kasva merkittävästi, ellei kaikkia vastauksia tallenneta muistiin (optioksi CSV/JSON).

## Lähteet
- [Python socket documentation](https://docs.python.org/3/library/socket.html)
- Wikipedia: [Banner grabbing](https://en.wikipedia.org/wiki/Banner_grabbing)
- Nmap Project: [Nmap Project](https://nmap.org)

