#!/usr/bin/env python
# игра "Калькулятор"


import brain_games.games.brain_calc_logic as calc
from brain_games.game_engine import engine


def main():
    engine(calc.TASK, calc.game_logic)


if __name__ == '__main__':
    main()
