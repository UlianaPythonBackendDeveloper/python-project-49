"""Calculator game."""

import random
from brain_games.cli import welcome_user


def calculate(num1: int, num2: int, operation: str) -> int:
    """Calculate result of operation between two numbers."""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    else:
        raise ValueError(f"Unknown operation: {operation}")


def run_calc_game() -> None:
    """Run the calculator game."""
    name = welcome_user()  # ← Используем функцию из cli.py
    
    print("What is the result of the expression?")
    
    rounds_count = 3
    
    for _ in range(rounds_count):
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operation = random.choice(['+', '-', '*'])
        
        question = f"{num1} {operation} {num2}"
        correct_answer = str(calculate(num1, num2, operation))
        
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


def main() -> None:
    """Main function to start the calculator game."""
    run_calc_game()


if __name__ == "__main__":
    main()