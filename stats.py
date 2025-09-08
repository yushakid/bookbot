def count_words(text: str):
    words = text.split(" ")
    count = len(words)
    return count

def num_words(text: str):
    letters = {}
    for letter in text:
        letter = letter.lower()
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

if __name__ == "__main__":
    print(num_words("holy wow"))