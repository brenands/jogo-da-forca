import random


def get_random_name() -> str:
    file = open('C:\\Users\\Brenand\\PycharmProjects\\jogodavelha\\Jogo-da-velha\\files\\words.txt', 'r')
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()
    number = random.randrange(0, len(words))
    secret_word = words[number].lower()

    return secret_word

