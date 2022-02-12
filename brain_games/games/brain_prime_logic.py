# логика игры "Проверка на четность"

from random import randint


def game_logic():
    question_string = ('Answer "yes" if given number is prime.'
                       ' otherwise answer "no".')
    question = randint(1, 100)
    count = 0
    i = question // 2

    # print('Вопрос: ' + str(question))

    while i > 0:
        # print('Итерация ' + str(int((question / 2 - i))) +
        #      ' ::: ' + str(question) + ' / ' + str(i) +
        #      ' = ' + str(question / i) + ' ' + 'Count: ' + str(count))

        if question % i == 0:
            count += 1
            i -= 1
            if count > 1:
                right_answer = 'no'
                return (question_string, question, right_answer)
        else:
            i -= 1

    right_answer = 'yes'

    return (question_string, question, right_answer)
