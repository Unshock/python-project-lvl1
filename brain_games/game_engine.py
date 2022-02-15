import prompt


def engine(TASK, q_and_a):

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name)

    print(TASK)

    i = 0
    while i < 3:
        print('Question: ' + str(q_and_a[i][0]))
        answer = prompt.string('Your answer: ')
        if answer == str(q_and_a[i][1]):
            print('Correct!')
            i += 1
            if i == 3:
                print('Congratulations, ' + name + '!')

        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
                  "Let's try again, {}!"
                  .format(answer, str(q_and_a[i][1]), str(name)))
            i = 3
