def get_num_words(words: str): 
    num_words = words.split()
    return len(num_words)

def get_num_characters(words: str) -> list:
    characters = []

    for char in words:
        if char.isalpha():
            char = char.lower()
            found = False
            for character in characters:
                if character["char"] == char:
                    character["num"] += 1
                    found = True
                    break
            if not found:
                characters.append({"char": char, "num": 1})

    return characters

def sort_on(dict: dict):
    return dict["num"]