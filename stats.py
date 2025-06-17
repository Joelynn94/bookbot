def get_num_words(words: str): 
    num_words = words.split()
    return len(num_words)

def get_num_characters(words: str):
    characters = {}

    for i in range(len(words)):
        lower_char = words[i].lower()
        # print(lower_char)
        if lower_char not in characters:
            # print("Key '{lower_char}' does not exists in the dictonary")
            characters[lower_char] = 1
        else: 
            # print(f"Key '{lower_char}' exists in dictonary")
            characters[lower_char] += 1

    return characters