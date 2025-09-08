def count_words(text: str):
    words = text.split(" ")
    count = len(words)
    return count

def num_words(text: str):
    num = len(text)
    return num

if __name__ == "__main__":
    print(num_words("holy wow"))