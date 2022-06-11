import unidecode
import re


def change_word_to_underline(secret_word):
    letters_right = ["_" for line in secret_word]
    # letters_right = ' '.join(letters_right)
    return letters_right


def remove_special_characters(secret_word):
    secret_word_new = unidecode.unidecode(secret_word)
    secret_word_new = re.sub('-', '', secret_word_new)

    return secret_word_new


def parse_input():
    kick = input('Escolha uma letra: ')
    kick = kick.strip().lower()

    return kick


def check_if_exists_on_word(word, letter):
    if letter in word:
        return True


def show_correct_letters(secret_word, kick, letters_right):
    index = 0
    for letter in secret_word:
        if kick == letter:
            letters_right[index] = letter
        index += 1
    return letters_right
