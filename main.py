def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()

        words = get_words(file_contents)

        letter_count = get_letters_count(file_contents) 

        print_report(len(words), letter_count)

def get_words(file):
    return file.split()

def get_letters_count(file):
    letters_count = {}

    for letter in file:
        sanitezed_letter = letter.lower()

        if not sanitezed_letter.isalpha():
            continue

        if sanitezed_letter in letters_count:
            letters_count[sanitezed_letter] += 1
        else:
            letters_count[sanitezed_letter] = 1

    return letters_count

def print_report(words, letter_count):
    print('--- Begin report of books/frankenstein.txt ---')

    print(f"{words} words found in the document")
    print()

    sorted_letters = sort_letters(letter_count)

    for item in sorted_letters:
        print(f"The '{item['letter']}', character was found {item['count']} times")

def sort_on(letter):
    return letter['count']

def sort_letters(unsorted_letters):
    sorted_list = []
    for letter in unsorted_letters:
        sorted_list.append({'letter': letter, 'count': unsorted_letters[letter]})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()
