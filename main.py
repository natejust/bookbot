from stats import get_num_words
from stats import get_sorted_num_character
from stats import get_book_text
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = sys.argv[1]
    text = get_book_text(text)
    print(get_num_words(text))
    list = get_sorted_num_character(text)

    for entry in list:
        print(f"{entry['char']}: {entry['num']}")
main()