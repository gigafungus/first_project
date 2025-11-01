from brain_games.engine import start
from brain_games.games.game_prime import GAME_DESCRIPTION, prime


def main():
    start(GAME_DESCRIPTION, prime)


if __name__ == '__main__':
    main()
