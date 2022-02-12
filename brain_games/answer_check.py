import prompt


def answer_check(number_of_iterations, question, right_answer, name, i):
    print('Question: ' + str(question))
    answer = prompt.string('Your answer: ')

    if answer == str(right_answer):
        print('Correct!')
        i += 1
        if i > number_of_iterations:
            print('Congratulations, ' + name + '!')
            return i
        else:
            return i
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
              "Let's try again, {}!".format(answer, str(right_answer), str(name)))
        i = number_of_iterations + 1
        return i
