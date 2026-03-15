import prompt
import random

from brain_games.cli import welcome_user

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0 

    while correct_answers < 3:
        question = random.randint(1, 100)
        correct_answer = 'yes' if is_even(question) else 'no'

        print(f"Question: {question}")
        user_answer = prompt.string("You answer: ").lower().strip()

        if user_answer ==  correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer; (. ")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if correct_answers == 3:
        print(f"Congratulations, {name}!")
        
     
if __name__ == '__main__':
    main()