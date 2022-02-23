#!/usr/bin/env python
# игра "Простое ли число?"


import brain_games.games.prime_logic as prime
from brain_games.game_engine import run_engine


def main():
    run_engine(prime.TASK, prime.get_q_and_a)


if __name__ == '__main__':
    main()
