"""Module for user interaction in Brain Games."""


def welcome_user() -> None:
    """Greet the user and ask for their name."""
    print("Welcome to the Brain Games!")
    name =input("May I have your name?")
    print(f"Hello, {name}!")
    return name