import random


def play():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    file = open("words.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].lower()

    letters_right = ["_" for line in secret_word]

    hang = False
    hit = False
    miss = 0
    life = 6
    incorrect_letter = []

    print(letters_right)

    while not hang and not hit:

        kick = input("Qual letra? ")
        kick = kick.strip().lower()

        if kick in incorrect_letter:
            print('Essa letra já foi utilizada, tente novamente'
                  ' outra letra.')
        else:
            if kick in secret_word:
                index = 0
                for letra in secret_word:
                    if kick == letra:
                        letters_right[index] = letra
                    index += 1
            else:
                miss += 1
                life -= 1
                incorrect_letter.append(kick)
                print(f'Letras erradas {incorrect_letter}.')
                print(f'Voce ainda tem {life} vidas.')

            hang = miss == 6
            hit = "_" not in letters_right
            print(letters_right)

    if hit:
        print("Você ganhou!!")
    else:
        print("Você perdeu!!")
        print(f'A palavra secreta era {secret_word}.')
    print("Fim do jogo")


play()
