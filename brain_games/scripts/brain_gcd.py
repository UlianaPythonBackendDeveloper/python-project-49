"""Greatest Common Divisor game."""

import random
from brain_games.cli import welcome_user


def find_gcd(a: int, b: int) -> int:
    """
    Find the greatest common divisor of two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Greatest common divisor
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)


def run_gcd_game() -> None:
    """Run the greatest common divisor game."""
    name = welcome_user()
    
    print("Find the greatest common divisor of given numbers.")
    
    rounds_count = 3
    
    for _ in range(rounds_count):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        
        question = f"{num1} {num2}"
        correct_answer = str(find_gcd(num1, num2))
        
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
    """Main function to start the GCD game."""
    run_gcd_game()


if __name__ == "__main__":
    main()