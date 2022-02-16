#!/usr/bin/env python
# игра "Арифметическая прогрессия"


import brain_games.games.brain_progression_logic as progression
from brain_games.game_engine import engine


def main():
    engine(progression.TASK, progression.game_logic)


if __name__ == '__main__':
    main()
