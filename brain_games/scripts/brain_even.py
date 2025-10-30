from brain_games.engine import start
from brain_games.games.EVEN import GAME_DESCRIPTION, is_even


def main():
    start(GAME_DESCRIPTION, is_even)


if __name__ == "__main__":
    main()

