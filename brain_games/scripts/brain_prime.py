#!/usr/bin/env python
# игра "Простое ли число?"


import brain_games.games.brain_prime_logic as prime
from brain_games.game_engine import engine


def main():
    engine(prime.TASK, prime.q_and_a)


if __name__ == '__main__':
    main()
