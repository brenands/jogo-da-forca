import outputs
import random_words
import helpers

outputs.game_start()

secret_word = random_words.get_random_name()

secret_word = helpers.remove_special_characters(secret_word)

letters_right = helpers.change_word_to_underline(secret_word)

outputs.letters_right(letters_right)


hang = False
hit = False
life = 6
incorrect_letter = []

while not hang and not hit:
    kick = helpers.parse_input()
    check_letter = helpers.check_if_exists_on_word(secret_word, kick)

    if kick in incorrect_letter:
        outputs.letter_repeated()
    else:
        if check_letter:
            letters_right = helpers.show_correct_letters(secret_word, kick, letters_right)
        else:
            life -= 1
            incorrect_letter.append(kick)
            outputs.doesnt_exists()
            outputs.letters_tried(incorrect_letter)
            outputs.users_life(life)

        hang = life == 0
        hit = "_" not in letters_right
        outputs.letters_right(letters_right)

if hit:
    outputs.yoy_won()
else:
    outputs.you_lost()
