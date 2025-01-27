def main():
    with open ("./books/frankenstein.txt") as f:
        file_contents = f.read()

    wordCount(file_contents)
    
def wordCount(bookText):
    wordCountStr = bookText.split()
    totalWords = len(wordCountStr)
    print(f"{totalWords} words found in the document.")

main()