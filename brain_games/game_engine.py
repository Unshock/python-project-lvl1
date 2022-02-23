import prompt


def greet():
    print("Welcome to the Brain Games!")


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def run_engine(TASK, get_q_and_a):
    greet()
    name = welcome_user()

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

        if round_number == game_rounds_count - 1:
            print(f'Congratulations, {name}!')
