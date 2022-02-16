# Логика игры "Проверка на четность"

from random import randint


TASK = ('Answer "yes" if the number is even,'
        ' otherwise answer "no".')


def game_logic():

    question = randint(1, 100)

    if question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (question, right_answer)
