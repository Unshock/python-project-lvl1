#!/usr/bin/env python
# игра "Проверка на четность"


import brain_games.games.even_logic as even
from brain_games.game_engine import run_engine


def main():
    run_engine(even.TASK, even.get_q_and_a)


if __name__ == '__main__':
    main()
