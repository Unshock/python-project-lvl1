# Логика игры "Проверка на четность"

from random import randint


TASK = ('Answer "yes" if given number is prime. '
        'otherwise answer "no".')


def is_prime(question):
    if question == 1:
        return False
    else:
        count = 0
        for i in range(2, question // 2):
            if question % i == 0:
                count += 1
                if count > 0:
                    return False
    return True


def get_q_and_a():
    question = randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'

    return question, answer
