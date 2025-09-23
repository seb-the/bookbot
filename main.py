def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def wordcount(text):
    return len(text.split())


def main():
    text = get_book_text("./books/frankenstein.txt")
    print(f"Found {wordcount(text)} total words")

main()
