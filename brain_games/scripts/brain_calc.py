# игра "Калькулятор"


import brain_games.games.brain_calc_logic as calc
from brain_games.game_engine import engine


def main():
    engine(calc.TASK, calc.q_and_a)


if __name__ == '__main__':
    main()
