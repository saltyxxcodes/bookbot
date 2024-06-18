def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_counter = count_words(text)
    character_counter = count_characters(text)
    print(character_counter)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(besedilo):
    words = besedilo.split()
    return len(words)

def count_characters(besedilo):
    alphabet = {}
    for crka in besedilo:
        mala_crka = crka.lower()
        if mala_crka in alphabet:
            alphabet[mala_crka] += 1
        else:
            alphabet[mala_crka] = 1

    return alphabet
    
    
main()

