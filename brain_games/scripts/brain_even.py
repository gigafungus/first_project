from brain_games.engine import start
from brain_games.games.game_even import GAME_TASK, is_even


def main():
    start(GAME_TASK, is_even)


if __name__ == "__main__":
    main()

