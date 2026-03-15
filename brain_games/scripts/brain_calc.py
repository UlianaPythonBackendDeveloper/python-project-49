import random

from brain_games.cli import welcome_user

DISCRIPTION = "What is the result of the expression?"


def get_expression():
    number1 = random.randint(1, 25)
    number2 = random.randint(1, 25)
    operation = random.choice(['+', '-', '*'])
    question = f"{number1} {operation} {number2}"

    if operation == '+':
        correct = number1 + number2
    elif operation == '-':
        correct = number1 - number2
    else:
        correct = number1 * number2

    return str(correct), question


def main():
    name = welcome_user()
    print(DISCRIPTION)

    correct_answers = 0

    while correct_answers < 3:
        correct_answer, question = get_expression()

        print(f"Question: {question} ")
        user_answer = input("You answer: ").strip()

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer  (. ", end="")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

        if correct_answers == 3:
            print(f"Congratulations, {name}!")

if __name__ == '__main__':
    main()