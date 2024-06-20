def main():
    frankenstein_path = "../bookbot/books/frankenstein.txt"
    text = read_book(frankenstein_path)
    words = num_of_words(text)
    letter = num_of_letters(text)
    print(f"{words} words found in the document")
    print(letter)

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

