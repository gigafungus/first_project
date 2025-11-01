from brain_games.engine import start
from brain_games.games.game_progression import GAME_TASK, progression


def main():
    start(GAME_TASK, progression)


if __name__ == '__main__':
    main()
