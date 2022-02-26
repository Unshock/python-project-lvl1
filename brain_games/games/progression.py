# Логика игры "Арифметическая прогрессия"

from random import randint


TASK = 'What number is missing in the progression?'


def get_encrypted_progression(progression, encrypted_element):
    progression[encrypted_element:encrypted_element + 1] = ['..']
    question = ' '.join(map(str, progression))

    return question


def get_q_and_a():
    progression_length = 10
    start = randint(1, 50)
    step = randint(1, 5)
    encrypted_element = randint(0, progression_length - 1)

    progression = list(range(start, start + step * progression_length, step))
    answer = progression[encrypted_element]

    question = get_encrypted_progression(progression, encrypted_element)

    return question, answer
