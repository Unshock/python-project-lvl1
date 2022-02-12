# Логика игры "Арифметическая прогрессия"

from random import randint


def game_logic():

    question_string = 'What is the result of the expression?'
    i = 0
    question = ''
    row_range = randint(6, 12)
    first_number = randint(1, 50)
    number_raise = randint(1, 5)
    encrypted_element = randint(0, row_range - 1)

    while i <= row_range:

        # print('Итерация: ' + str(i - 1) + ' Ряд: ' + str(question))

        if encrypted_element == i:
            question = question + '.. '
            right_answer = first_number + (i * number_raise)
            i += 1

        else:
            question = question + str(first_number + (i * number_raise)) + ' '
            i += 1

    # print('row_range = ' + str(row_range) + '\n' +
    # 'Верный ответ ' + str(right_answer) + '\n' +
    # 'Кодовый элемент: ' + str(encrypted_element))

    return (question_string, question, right_answer)
