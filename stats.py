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

def sort_on(values: dict):
    return values["count"]

def sorted_letters(letters: dict):
    values = []
    for letter, count in letters.items():
        if letter.isalpha():
            values.append({"letter": letter, "count": count})
    values.sort(reverse = True, key = sort_on)

    print("============ BOOKBOT ============")
    print("Analyzing book\n----------- Word Count ---------\nFound 75767 total words\n--------- Character Count -------")
    for letter in values:
        print(f"{letter['letter']}: {letter['count']}")

if __name__ == "__main__":
    letters = num_words("hello holy cow!")
    sorted_letters(letters)

