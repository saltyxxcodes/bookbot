def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_counter = count_words(text)
    character_counter = count_characters(text)

    # Print header of the function with path variable wich tells us wich document we are reviewing
    print(f"--- Begin report of {book_path} ---")
    # Print how many words are in the given document
    print(f"{word_counter} words found in the document\n")
    # Print character counter
    for d in character_counter:
        print(d) 
    print("--- End report ---")

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
    
    seznam_crk = []
    for c, count in alphabet.items():
        if c.isalpha():
            seznam_crk.append({"char": c, "num": count})
    
    # Now we sort based on the count in reverse order
    seznam_crk.sort(reverse=True, key=sort_on)
    
    # After sorting, format the strings
    formatted_report = [
        f"The '{entry['char']}' character was found {entry['num']} times"
        for entry in seznam_crk
    ]
    return formatted_report

def sort_on(dict):
    return dict["num"]


main()

