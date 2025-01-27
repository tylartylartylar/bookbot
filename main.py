def main():
    with open ("./books/frankenstein.txt") as f:
        file_contents = f.read()

    characterCount = charCount(file_contents)
    wordCount = wordCounter(file_contents)
    print_report(wordCount, characterCount)

def print_report(words, characters):
    print('----- Beginning report on Frankenstein -----')
    print(f"there are {words} in the document")
    
    for char in characters:
        print(f"{characters[char]} is present {char} times")

def wordCounter(bookText):
    wordCountStr = bookText.split()
    totalWords = len(wordCountStr)
    return f"{totalWords} words found in the document."

def charCount(bookText):
    character_dic = {}
    lowercaseContents = bookText.lower()

    for char in lowercaseContents:
        if char in character_dic:
            character_dic[char] += 1
        else: 
            character_dic[char] = 1
    return character_dic



main()