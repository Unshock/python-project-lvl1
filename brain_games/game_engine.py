import prompt

NUMBER_OF_ITERATIONS = 3


def engine(TASK, game_logic):

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)

    print(TASK)

    i = 0
    while i < NUMBER_OF_ITERATIONS:
        q_and_a = game_logic()
        question = str(q_and_a[0])
        right_answer = str(q_and_a[1])

        print('Question: ' + question)
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
            i += 1
            if i == NUMBER_OF_ITERATIONS:
                print('Congratulations, ' + name + '!')

        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
                  "Let's try again, {}!"
                  .format(answer, right_answer, str(name)))
            i = NUMBER_OF_ITERATIONS
