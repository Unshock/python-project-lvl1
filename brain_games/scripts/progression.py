#!/usr/bin/env python
# игра "Арифметическая прогрессия"


import brain_games.games.progression_logic as progression
from brain_games.game_engine import run_engine


def main():
    run_engine(progression.TASK, progression.get_q_and_a)


if __name__ == '__main__':
    main()
