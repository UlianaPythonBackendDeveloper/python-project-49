import random
from brain_games.cli import welcome_user 


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_gcd_questions():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    correct_answer = str(gcd(number1, number2))
    question = f"{number1} {number2}"
    return correct_answer, question


def main():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")

    correct_answers = 0 

    while correct_answers < 3:
        correct_answer, question = get_gcd_questions()
        print(f"Question: {question}")
        user_answer  = input("You answer:")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. ")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if correct_answers == 3:
        print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()