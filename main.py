def main():
    frankenstein_path = "../bookbot/books/frankenstein.txt"
    text = read_book(frankenstein_path)
    words = num_of_words(text)
    letter = num_of_letters(text)

    letter_list = [{'letter': key, 'count': value} for key, value in letter.items()]
    letter_list.sort(key=lambda x: x["count"], reverse=True)

    print(f"--- Begin report of {frankenstein_path} ---")
    print(f"{words} words found in the document")
    for item in letter_list:
        print(f"The '{item['letter']}' character was found {item['count']} times")
    
    print("--- End report ---")

def num_of_words(text):
    words = text.split()
    word_count = len(words)
    return word_count


def read_book(text):
    with open(text) as f:
        return f.read()
    
def num_of_letters(letter):
    letter_dict = {}
    my_string = letter
    lowered_string = my_string.lower()
    for l in lowered_string:
        if l.isalpha():
            letter_dict[l] = letter_dict.get(l, 0) + 1
    return letter_dict


main()

