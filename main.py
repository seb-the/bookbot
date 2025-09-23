# count words in string
from stats import wordcount

# count characters in string, return as dict (character : count)
from stats import count_characters

# turn book file into string
def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    text = get_book_text("./books/frankenstein.txt")
    print(f"Found {wordcount(text)} total words")
    print(count_characters(text))

main()
