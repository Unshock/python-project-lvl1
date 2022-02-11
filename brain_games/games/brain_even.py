#игра "Проверка на четность"
import prompt
from random import randint

def greet():
    print("Welcome to the Brain Games!")


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)
    return name
    

def is_even():
    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1

    while i < 4:
        question_number = randint(1, 100)
        if question_number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'

        print('Question: ' + str(question_number))
        answer = prompt.string('Your answer: ')

        if answer == right_answer:
            print('Correct!')
            i += 1
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
            "Let's try again, {}!".format(answer, right_answer, name))
            return
    print('Congratulations, ' + name + '!')


def main():
    greet()
    is_even()

if __name__ == '__main__':
    main()
