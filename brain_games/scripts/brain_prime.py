#!/usr/bin/env python
# игра "Простое ли число?"


import brain_games.games.prime as prime
from brain_games.engine import run_engine


def main():
    run_engine(prime.TASK, prime.get_q_and_a)


if __name__ == '__main__':
    main()
