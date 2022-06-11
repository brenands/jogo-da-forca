def game_start():
    print('*********************************')
    print('***Bem vindo ao jogo da Forca!***')
    print('*********************************')


def you_lost():
    print("Você perdeu, não foi dessa vez!!")


def yoy_won():
    print('Parabéns, você ganhou!!')


def reveal_secret_word(word):
    print(f'A palavra secreta era {word}.')


def doesnt_exists():
    print('Esta letra não existe, tente novamente.')


def users_life(life):
    print(f'{life} Vidas restantes.')


def letters_tried(letters):
    print(f'Letras erradas: {letters}.')


def letters_right(word):
    print(f'Palavra secreta: {word}')


def letter_repeated():
    print('Essa letra já foi utilizada, tente novamente outra letra.')
