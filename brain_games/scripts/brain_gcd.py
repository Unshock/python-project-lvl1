#!/usr/bin/env python
# Игра "Наибольший общий делитель"

import brain_games.games.brain_gcd_logic as gcd
from brain_games.game_engine import engine


def main():
    engine(gcd.TASK, gcd.q_and_a)


if __name__ == '__main__':
    main()
