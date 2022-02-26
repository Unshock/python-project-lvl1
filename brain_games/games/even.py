# Логика игры "Проверка на четность"

from random import randint


TASK = ('Answer "yes" if the number is even, '
        'otherwise answer "no".')


def get_q_and_a():

    question = randint(1, 100)

    answer = 'yes' if not question % 2 else 'no'

    return question, answer
