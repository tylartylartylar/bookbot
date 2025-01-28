def main():
    with open ("./books/frankenstein.txt") as f:
        file_contents = f.read()

    characterCount = charCount(file_contents)
    wordCount = wordCounter(file_contents)

    print_report(wordCount, characterCount)

# This doesn't work. This should print a nicely formatted overview of word count, character counts sorted by number of occurances.
def print_report(words, characters):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{words}\n")
    for char_tuple in characters:
        letter = char_tuple[0]
        count = char_tuple[1]
        print(f"The '{letter}' character was found {count} times")
    
    print('--- End report ---')


# 
def wordCounter(bookText):
    wordCountStr = bookText.split() # Creates a list of strings (words) found in the bookText
    totalWords = len(wordCountStr)  # The length of the list
    return f"{totalWords} words found in the document" # Returns the length of the list.


# ===== Get Character Count =====
def charCount(bookText):
    character_dic = {} # define the dictionary for character and it's count.
    lowercaseContents = bookText.lower() # formats all chars into lowercase. 

    for char in lowercaseContents:
        if char in character_dic:
            character_dic[char] += 1
        else: 
            character_dic[char] = 1
    
    filtered_dic = {k: v for k, v in character_dic.items() if k.isalpha()}
    sorted_dic = sorted(filtered_dic.items(), key=lambda x: x[1], reverse=True)

    return sorted_dic
# ===== Get Character Count =====


main()