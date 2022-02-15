# логика игры "Проверка на четность"

from random import randint


def game_logic():
    TASK = ('Answer "yes" if the number is even,'
            ' otherwise answer "no".')
    question = randint(1, 100)

    if question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return TASK, (question, right_answer)


TASK = game_logic()[0]
q_and_a = (game_logic()[1], game_logic()[1], game_logic()[1])
