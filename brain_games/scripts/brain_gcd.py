from brain_games.engine import start
from brain_games.games.game_gcd import GAME_TASK, gcd


def main():
    start(GAME_TASK, gcd)


if __name__ == "__main__":
    main()

