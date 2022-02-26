#!/usr/bin/env python
# игра "Проверка на четность"


import brain_games.games.even as even
from brain_games.engine import run_engine


def main():
    run_engine(even.TASK, even.get_q_and_a)


if __name__ == '__main__':
    main()
