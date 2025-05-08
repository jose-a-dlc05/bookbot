from stats import get_word_count, get_character_count, get_char_count_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def print_book_report(book_path, word_count, char_count_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in char_count_list:
        if(dict['char'].isalpha()):
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")
            
            


def main():
    if(len(sys.argv) is not 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    character_count = get_character_count(book_text)
    char_count_list = get_char_count_list(character_count)
    print_book_report(book_path, word_count, char_count_list)



main()