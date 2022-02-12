# игра "Проверка на четность"

import prompt
from brain_games.games.brain_gcd_logic import game_logic
from brain_games.cli import welcome_user
from brain_games.greet import greet
from brain_games.answer_check import answer_check


def game():
    name = welcome_user()

    question_string, question, right_answer = game_logic()

    print(str(question_string))

    i = 1

    while i < 4:

        question_string, question, right_answer = game_logic()
        print('Question: ' + str(question))
        answer = prompt.string('Your answer: ')
        if answer_check(answer, right_answer, name, i):
            i += 1
        else:
            return

    print('Congratulations, ' + name + '!')


def main():
    greet()
    game()


if __name__ == '__main__':
    main()
