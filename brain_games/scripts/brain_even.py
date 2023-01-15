#!/usr/bin/env python3
# Тут должен быть импорт логики игры!!!!
from brain_games.game import even_game
import brain_games.engine


def main():
    brain_games.engine.main(even_game)


if __name__ == '__main__':
    main()
