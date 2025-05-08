def get_word_count(book):
    book_words_list = book.split()
    book_word_count = len(book_words_list)
    return book_word_count

def get_character_count(book):
    book_words_list = book.split()
    book_character_count = {}
    for i in range(0, len(book_words_list)):
        book_words_list_lower = book_words_list[i].lower()
        for char in book_words_list_lower:
            if char in book_character_count:
                book_character_count[char] += 1
            else:
                book_character_count[char] = 1
    return book_character_count

def sort_on(dict):
    return dict["num"]

def get_char_count_list(book_character_count):
    sorted_list = []
    for k, v in book_character_count.items():
        sorted_list.append({"char": k, "num": v})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
                        
    
        