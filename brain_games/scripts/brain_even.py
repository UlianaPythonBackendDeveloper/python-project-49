"""Even number game."""

import random
from brain_games.cli import welcome_user


def is_even(number: int) -> bool:
    """Check if number is even."""
    return number % 2 == 0


def run_even_game() -> None:
    """Run the even number checking game."""
    name = welcome_user()  # ← Тоже используем cli.py
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    rounds_count = 3
    
    for _ in range(rounds_count):
        number = random.randint(1, 100)
        
        print(f"Question: {number}")
        user_answer = input("Your answer: ").strip().lower()
        
        correct_answer = "yes" if is_even(number) else "no"
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


def main() -> None:
    """Main function to start the even game."""
    run_even_game()


if __name__ == "__main__":
    main()