# count words in string
from stats import wordcount

# count characters in string, return as dict (character : count)
from stats import count_characters

from stats import convert_dict_to_list

from stats import sort_by_num

# turn book file into string
def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    text = get_book_text("./books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount(text)} total words")
    print("--------- Character Count -------")
    characters = count_characters(text)
    list_of_dictionaries = convert_dict_to_list(characters)
    sorted_list = sort_by_num(list_of_dictionaries)
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()
