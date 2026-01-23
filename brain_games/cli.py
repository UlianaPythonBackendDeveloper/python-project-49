"""Module for user interaction in Brain Games."""
import prompt


def welcome_user() -> None:
    """Greet the user and ask for their name."""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name?")
    print(f"Hello, {name}!")
