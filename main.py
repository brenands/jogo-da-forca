from functions import outputs
from functions import helpers
from functions import random_words

outputs.game_start()
word = random_words.get_random_name()
word = helpers.remove_special_characters(word)
letters_right = helpers.change_word_to_underline(word)
outputs.letters_right(letters_right)

hang = False
hit = False
life = 6
incorrect_letter = []
tries = []

while not hang and not hit:
    kick = helpers.parse_input()
    check_letter = helpers.check_if_exists_on_word(word, kick)

    if kick in incorrect_letter:
        outputs.letter_repeated()
    else:
        if check_letter:
            tries.append(kick)
            letters_right = helpers.show_correct_letters(word, tries)
        else:
            life -= 1
            incorrect_letter.append(kick)
            outputs.doesnt_exists(kick)
            outputs.draw_hangman(life)
            outputs.letters_tried(incorrect_letter)
            outputs.users_life(life)

        hang = life == 0
        hit = "_" not in letters_right
        outputs.letters_right(letters_right)

if hit:
    outputs.yoy_won()
else:
    outputs.you_lost()
    outputs.reveal_secret_word(word)
