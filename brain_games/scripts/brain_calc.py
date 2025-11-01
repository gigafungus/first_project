from brain_games.engine import start
from brain_games.games.game_calc import GAME_TASK, expression


def main():
    start(GAME_TASK, expression)


if __name__ == "__main__":
    main()

