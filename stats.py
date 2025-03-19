def wordCounter(bookText):
    wordCountStr = bookText.split()
    totalWords = len(wordCountStr)
    return f"{totalWords} words found in the document"

def count_chars(text):
    chars = {}
    lowercase_text = text.lower()
    
    for char in lowercase_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
            
    return chars

def sort_chars(char_counts):
    # Create a list of dictionaries with character and count
    sorted_list = []
    for char, count in char_counts.items():
        sorted_list.append({"char": char, "count": count})
    
    # Sort the list by count, from greatest to least
    sorted_list.sort(key=lambda x: x["count"], reverse=True)
    
    return sorted_list