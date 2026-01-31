import random
from brain_games.cli import welcome_user

def is_even(number: int) -> bool:
    return number % 2 == 0

def run_even_game() -> None:
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer_neded = 3
    correct_answer_count = 0
    
    while correct_answer_count < correct_answer_neded:
        number = random.randint(1, 100)
        
        print(f"Question: {number}")
        user_answer = input("You answer: ").strip().lower()
        correct_answer = "yes" if is_even(number)else "no"
        
        if user_answer == correct_answer:
            print("Correct")
            correct_answer_count += 1
        else:
            print("f'{user_answer}'is wrong answer; (. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations,{name}!")
    
def main()->None:
    run_even_game()
    
if __name__ == '__main__':
    main()