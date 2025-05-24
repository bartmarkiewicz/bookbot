from stats import number_of_words, char_count, get_sorted_dict_list
import sys

def get_book_text(filePath):
    print(f"Analyzing book found at {filePath}")
    with open(filePath, 'r') as f:
        return f.read();



def main(bookPath):
    print("============ BOOKBOT ============")
    bookText = get_book_text(bookPath)
    print("----------- Word Count ----------")
    print(f"Found {number_of_words(bookText)} total words")
    charDict = char_count(bookText)
    print("--------- Character Count -------")
    sortedDicts = get_sorted_dict_list(charDict)
    for dict in sortedDicts:
        if dict["char"].isalpha() and dict["char"] != " ":
            print(f"{dict["char"]}: {dict["num"]}")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main(sys.argv[1])