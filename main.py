import sys
from stats import get_num_words, get_num_characters, sort_on

def get_book_text(file_path: str): 
    file_contents = ""
    with open(file_path) as file:
        print(f"Analyzing book found at {file_path}...")
        file_contents = file.read()

    return file_contents



def main():
    if len(sys.argv) <= 1:
        print("Usage: python main.py <book_path>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    contents = get_book_text(book_path)
    
    print("--------- Word Count ----------")
    words = get_num_words(contents)
    print(f"Found {words} total words")

    characters = get_num_characters(contents)
    characters.sort(reverse=True, key=sort_on)
    print("--------- Character Count ----------")
    for char_dict in characters:
        print(f"'{char_dict['char']}': {char_dict['num']}")

if __name__ == '__main__':
    main()