from src.trie import Trie
from src.corrector import suggest_correction

def main():
    trie = Trie()
    words = ["kissa", "koira", "kana", "kala", "kirja", "kivi"]

    for i in words:
        trie.insert(i)
    
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