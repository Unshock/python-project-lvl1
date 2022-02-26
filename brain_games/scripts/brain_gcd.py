#!/usr/bin/env python
# игра "Наибольший общий делитель"


import brain_games.games.gcd as gcd
from brain_games.engine import run_engine


def main():
    run_engine(gcd.TASK, gcd.get_q_and_a)


if __name__ == '__main__':
    main()
