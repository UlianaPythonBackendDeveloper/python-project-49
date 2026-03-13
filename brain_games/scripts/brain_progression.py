import random
from brain_games.cli import welcome_user

DESCRIPTION = "What number is missing in the progression?"

def generate_progression():
    length = random.randint(5,10)
    start = random.randint(1,50)
    step = random.randint(2,10)

    missing_idx = random.randint(0, length -1)

    progression = []
    for i in range(length):
        number = start + i * step
        progression.append(str(number))

    correct_answer = progression[missing_idx]
    progression[missing_idx] = ".."

    question = " ".join(progression)
    return correct_answer,question

def main():
    name = welcome_user()
    print(DESCRIPTION)

    correct_answers = 0

    while correct_answers < 3:
        correct_answer, question = generate_progression()
        print(f"Question: {question}")
        user_answer = input("You answer: ")

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