from stats import count_words, num_words

def get_book_text(filename: str):
    with open(filename, 'r', encoding = "UTF-8") as f:
        text = f.read()
    return text

def main():
    text = get_book_text("books/frankenstein.txt")
    print(num_words(text))

main()
