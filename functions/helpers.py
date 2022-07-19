import unidecode
import re


def change_word_to_underline(word) -> str:
    letters_right = ["_" for line in word]
    letters_right = ' '.join(letters_right)
    return letters_right


def remove_special_characters(word) -> str:
    secret_word_new = unidecode.unidecode(word)
    secret_word_new = re.sub('-', '', secret_word_new)
    return secret_word_new


def check_if_exists_on_word(word, letter) -> bool:
    return remove_special_characters(letter) in remove_special_characters(word)


def show_correct_letters(word, tries) -> str:
    letters_right = ["_" for line in word]

    for index, letter in enumerate(word):
        for item in tries:
            if remove_special_characters(item) == remove_special_characters(letter):
                letters_right[index] = letter

    letters_right = ' '.join(letters_right)
    return letters_right


def parse_input() -> str:
    kick = input('Escolha uma letra: ')
    kick = kick.strip().lower()
    return kick
