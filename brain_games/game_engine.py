import prompt


def run_engine(TASK, get_q_and_a):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print(TASK)

    game_rounds_count = 3

    for round_number in range(0, game_rounds_count):

        q_and_a = get_q_and_a()
        question = str(q_and_a[0])
        answer = str(q_and_a[1])

        print('Question: ' + question)
        player_answer = prompt.string('Your answer: ')

        if answer == player_answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.\n"
                  "Let's try again, {}!"
                  .format(player_answer, answer, str(name)))
            break
    else:
        print(f'Congratulations, {name}!')
