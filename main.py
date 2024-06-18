def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_counter = count_words(text)
    print(f"{word_counter} words found in the document")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(besedilo):
    words = besedilo.split()
    return len(words)

main()

