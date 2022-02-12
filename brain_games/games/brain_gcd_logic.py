# логика игры "Наибольший общий делитель"

from random import randint


def game_logic():
    question_string = 'Find the greatest common divisor of given numbers.'

    num1 = randint(20, 35)
    num2 = randint(5, 25)
    question = str(num1) + ' ' + str(num2)
    i = max(num1, num2)

    while i > 0:
        # отладочная печать
        # print('Итерация ' + str(i) + '; num1 = '
        # + str(num1) + '; num2 = ' + str(num2))

        if num1 % i == 0 and num2 % i == 0:
            right_answer = str(i)
            i = 0
        else:
            i -= 1

    return (question_string, question, right_answer)