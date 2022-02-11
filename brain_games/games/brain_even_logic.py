# логика игры "Проверка на четность"

from random import randint

def game_logic():
    question_string ='Answer "yes" if the number is even, otherwise answer "no".'
    question = randint(1, 100)
          
    if question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return (question_string, question, right_answer)

question_string, question, right_answer= game_logic()
