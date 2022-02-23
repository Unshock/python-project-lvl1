# Логика игры "Калькулятор"

from random import randint, choice
import operator


TASK = 'What is the result of the expression?'


def get_q_and_a():
    number_1 = randint(10, 30)
    number_2 = randint(5, 20)

    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    q_and_a_operator = choice(list(operations.keys()))

    question = f'{str(number_1)} {q_and_a_operator} {str(number_2)}'

    answer = operations[q_and_a_operator](number_1, number_2)

    return question, answer
