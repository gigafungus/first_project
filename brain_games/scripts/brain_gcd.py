from brain_games.engine import start
from brain_games.games.game_gcd import GAME_DESCRIPTION, gcd


def main():
    start(GAME_DESCRIPTION, gcd)


if __name__ == "__main__":
    main()

