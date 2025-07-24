from src.trie import Trie
from src.corrector import suggest_correction

def get_dict(file_name):
    """Lue sanat tiedostosta ja palauta listana."""
    with open(file_name, "r", encoding="utf-8") as f:
        return [i.strip() for i in f if i.strip()]

def main():
    trie = Trie()
    file = get_dict("dictionary.txt")
    
    for word in file:
        trie.insert(word)
    
    print("Kirjoitusvirheiden korjaaja")
    print("Anna sana, jolle haluat korjausehdotuksia.")
    print("Tyhjä syöte lopettaa ohjelman.\n")
    
    while True:
        word = input("Anna sana: ")
        if word == "":
            break
        
        suggestions = suggest_correction(trie, word)
        print("Korjausehdotukset:")
        for i in suggestions:
            print(f"- {i}")
        print()

if __name__ == "__main__":
    main()