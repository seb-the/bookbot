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
