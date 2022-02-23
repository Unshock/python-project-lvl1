# Логика игры "Наибольший общий делитель"

from random import randint


TASK = 'Find the greatest common divisor of given numbers.'


def get_gcd(number_1, number_2):

    i = min(number_1, number_2)

    while i > 0:
        if number_1 % i == 0 and number_2 % i == 0:
            answer = str(i)
            return answer
        else:
            i -= 1


def get_q_and_a():
    number_1 = randint(20, 35)
    number_2 = randint(5, 25)
    question = f'{str(number_1)} {str(number_2)}'

    answer = get_gcd(number_1, number_2)

    return question, answer
