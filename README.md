# BGTool
BGTool kirjoitusvirheiden korjaaja suomenkielisille sanoille. Hyödynnämme algoritmeja kuten Trie-rakennetta ja Damerau–Levenshtein-etäisyyttä. 

## Riippuvuudet
```bash
poetry install
```
## Käynnistys
Aja ohjelma projektin juuresta:
```bash
python -m src.main
```

## Testaus
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