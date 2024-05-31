import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

list_lowercase = list(string.ascii_lowercase)

def make_book_into_letters(l):
    return list("".join(l).lower())

def character_count(lowercase_letters, book_letters):
    char_dict = {letter: 0 for letter in lowercase_letters}
    for l in book_letters:
        if l in char_dict:
            char_dict[l] += 1
    return char_dict

def convert_into_list_of_dicts(chars_dict):
    return [{"name": name, "num": chars_dict[name]} for name in chars_dict]      




file_contents = main()
words = file_contents.split()
words_number = len(words)
book_letters = make_book_into_letters(words)
char_count = character_count(list_lowercase, book_letters)
list_of_dictionaries = convert_into_list_of_dicts(char_count)
sorted_list = sorted(list_of_dictionaries, key=lambda d: d["num"], reverse=True)
print("---Begin report of books/frankenstein.txt---")
print(f"{words_number} words found in the document\n")

for d in sorted_list:
    print(f"The {d["name"]} character was found {d["num"]} times")

print("--- End report ---")





