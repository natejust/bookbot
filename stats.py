def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    

def get_num_words(text):
    length = len(text.split())
    return f"Found {length} total words"

def get_num_character(text):
    text = text.lower()
    dictionary = {}
    for char in text:
        if not char.isalpha():
            continue
        if char not in dictionary:
            dictionary[char] = 0
        dictionary[char] +=1

    return dictionary

def get_sorted_num_character(text):
    characters = get_num_character(text)
    characters_list = [{"char": char, "num": count}
                       for char, count in characters.items() if char.isalpha()]
    def sort_on(items):
        return items["num"]
    
    characters_list.sort(key=sort_on, reverse=True)
    return characters_list

