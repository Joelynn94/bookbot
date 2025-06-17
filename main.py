import sys
from stats import get_num_words, get_num_characters

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
    print("--------- Character Count ----------")
    for char, count in characters.items():
        print(f"'{char}': {count}")

if __name__ == '__main__':
    main()