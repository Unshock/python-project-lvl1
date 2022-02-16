#!/usr/bin/env python
# игра "Проверка на четность"


import brain_games.games.brain_even_logic as even
from brain_games.game_engine import engine


def main():
    engine(even.TASK, even.game_logic)


if __name__ == '__main__':
    main()
