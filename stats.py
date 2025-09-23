def wordcount(text):
    return len(text.split())

def count_characters(text):
    characters = {}
    text = text.lower()
    for i in range(0, len(text)):
        if text[i] not in characters:
            characters[text[i]] = 1
        else:
            characters[text[i]] += 1
    return characters

# takes dict and returns list of dicts
def convert_dict_to_list(characters):
    list = []
    for char in characters:
        list.append({"char": char, "num": characters[char]})
    return list

# takes list of dicts and sorts the list by "num"
def sort_by_num(list):
    return sorted(list, key=lambda x: x["num"])

