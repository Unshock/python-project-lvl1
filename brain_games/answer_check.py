def answer_check(answer, right_answer, name, i):
    if answer == str(right_answer):
        print('Correct!')
        return True
    else:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
              "Let's try again, {}!"
              .format(answer, str(right_answer), str(name)))
        return False
