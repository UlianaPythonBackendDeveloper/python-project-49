"""Entry point for Brain Games."""
from brain_games.cli import welcome_user


def main() -> None:
    """Main function to start the game."""
    welcome_user()

if __name__ == "__main__":
    main()
