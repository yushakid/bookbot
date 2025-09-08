from stats import count_words, num_words, sorted_letters
import sys

def get_book_text(filename: str):
    with open(filename, 'r', encoding = "UTF-8") as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) < 2:
        print("USAGE: python3 main.py ,path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    letters = num_words(text)
    sorted_letters(letters)
main()
