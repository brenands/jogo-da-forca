import random
import os


def get_random_name() -> str:
    fn = os.path.join(os.path.dirname(__file__), '../files/words.txt')
    file = open(fn, 'r')
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()
    number = random.randrange(0, len(words))
    secret_word = words[number].lower()

    return secret_word

