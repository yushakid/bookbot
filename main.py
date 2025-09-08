def get_book_text(filename: str):
    with open(filename, 'r', encoding = "UTF-8") as f:
        text = f.read()
    return text

def count_words(text: str):
    words = text.split(" ")
    count = len(words)
    return count

def main():
    text = get_book_text("books/frankenstein.txt")
    print(count_words(text))

main()
