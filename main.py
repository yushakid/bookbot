import os

def get_book_text(filename: str):
    print("Reading file at:", os.path.abspath(filename))
    with open(filename, 'r') as f:
        text = f.read()
    print("Length of text:", len(text))
    return text

def main():
    print(get_book_text("books/frankenstein.txt")[:500])  # first 500 chars

main()