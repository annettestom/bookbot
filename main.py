import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def number_of_words(s):
    word_count = 0
    words = s.split()
    for word in words:
        word_count += 1
    return word_count

list_lowercase = list(string.ascii_lowercase)

def make_book_into_letters(l):
    new_list = []
    for word in l:
        for letter in word:
            new_list.append(letter)
    return new_list

def character_count(lowercase_letters, book_letters):
    count_values = []
    for letter in lowercase_letters:
        count = 0
        for l in book_letters:
            if letter == l:
                count += 1
        count_values.append(count)
    char_dict = dict(zip(lowercase_letters, count_values))
    return char_dict

def convert_into_list_of_dicts(dict):
    list_of_dicts= []
    for name in dict:
        new_dict = {}
        num = dict[name]
        new_dict["name"] = name 
        new_dict["num"] = num
        list_of_dicts.append(new_dict)
    return list_of_dicts
        



    
word_number = number_of_words(main())
book_letters = [x.lower() for x in make_book_into_letters(main().split())]
char_count = character_count(list_lowercase, book_letters)
list_of_dictionaries = convert_into_list_of_dicts(char_count)
sorted_list = sorted(list_of_dictionaries, key=lambda d: d["num"], reverse =True)
print("---Begin report of books/frankenstein.txt---")
print(f"{word_number} words found in the document\n")

for d in sorted_list:
    print(f"The {d["name"]} character was found {d["num"]} times")

print("--- End report ---")





