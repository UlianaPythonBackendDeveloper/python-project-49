import random
from brain_games.cli import welcome_user

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_prime_question():
    number = random.randint(2, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    question = str(number)
    return correct_answer, question


def main():
    name = welcome_user()
    print(DESCRIPTION)

    correct_answers = 0
    while correct_answers < 3:
        correct_answer, question = get_prime_question()
        print(f"Question: {question}")
        user_answer = input("You answer: ")

        if user_answer.lower() == correct_answer:
            print("Correct")
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