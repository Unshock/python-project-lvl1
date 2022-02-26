#!/usr/bin/env python
# игра "Калькулятор"


import brain_games.games.calc as calc
from brain_games.engine import run_engine


def main():
    run_engine(calc.TASK, calc.get_q_and_a)


if __name__ == '__main__':
    main()
