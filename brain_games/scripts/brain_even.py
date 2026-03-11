import prompt
import random

from brain_games.cli import welcome_user

DESCTRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def is_even(number):
    return number % 2 == 0


def brain_even():
    name = welcome_user()
    print(DESCTRIPTION)
    
    correct_answers = 0
    
    while correct_answers < 3:
        question = random.randint(1, 100)
        print(f"Question: {question}")
        answer = prompt.string("You anwser: ").lower()
        
        if answer == correct_answers:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answers}'.")
            print(f"Let's try again, {name}!")
            return
        
        print(f"Congratulations,{name}!")
        
if __name__ == '__main__':
    brain_even()