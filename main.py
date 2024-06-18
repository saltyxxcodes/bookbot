def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    stevilo_besed = 0
    for word in words:
        stevilo_besed += 1
    print(stevilo_besed)


main()