import sys
        
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        imported_book = sys.argv[1]
        from stats import get_num_characters, get_num_words
        print("============ BOOKBOT ============")
        print("Analyzing book found at " + imported_book)

        print("----------- Word Count ----------")
        print(f'Found {get_num_words(imported_book)} total words')

        print("--------- Character Count -------")
        char_list = get_num_characters(imported_book)
        for item_dict in char_list:
            print(f'{item_dict["character"]}: {item_dict["num"]}')
        sys.exit(0)

main()