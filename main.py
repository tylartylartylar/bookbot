import sys
from stats import wordCounter, count_chars, sort_chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    # Check if a book path was provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get the book path from command line arguments
    path = sys.argv[1]
    
    # Get the book text
    file_contents = get_book_text(path)
    
    # Calculate word count and character counts
    word_count = wordCounter(file_contents).split()[0]  # Extract just the number
    char_counts = count_chars(file_contents)
    sorted_chars = sort_chars(char_counts)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    # Print only alphabetical characters
    for item in sorted_chars:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()