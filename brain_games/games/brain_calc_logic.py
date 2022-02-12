# Логика игры "Калькулятор"

from random import randint


def game_logic():
    question_string = 'What is the result of the expression?'

    num1 = randint(10, 30)
    num2 = randint(5, 20)

    question_pull = (str(num1) + ' + ' + str(num2), str(num1) +
                     ' - ' + str(num2), str(num1) + ' * ' + str(num2))
    question_type = randint(0, 2)

    question = question_pull[question_type]

    if question_type == 0:
        right_answer = num1 + num2
    elif question_type == 1:
        right_answer = num1 - num2
    else:
        right_answer = num1 * num2

    return (question_string, question, right_answer)
