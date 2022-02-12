# игра "Арифметическая прогрессия"

from brain_games.games.brain_progression_logic import game_logic
from brain_games.cli import welcome_user
from brain_games.greet import greet
from brain_games.answer_check import answer_check


def game():
    name = welcome_user()

    print(game_logic()[0])

    i = 1
    number_of_iterations = 3

    while i <= number_of_iterations:
        question, right_answer = game_logic()[1:]

        i = answer_check(number_of_iterations,
                         question, right_answer, name, i)


def main():
    greet()
    game()


if __name__ == '__main__':
    main()
