'''
1. It should read your name
2. It should ask a question( what is square of number- Select any number between 1-100)
3. If users answer is right then score increased by +10
4. If wrong answer score should decreased by -5
5. It should ask questions again and again but after ansering to quest also after updating score
6. It should ask (do u want to continue quiz or not?) if yes continue
if no come out of quiz by displaying "LOOSER"
7. it may ask ("What is the square root of a perfect square number- {1-1000}")
8. Keep tracking the time at the time of giving player name
9. Calculate the answering time for each question by player
'''

import random
from datetime import datetime
from MyPackagesDay5 import exceptions, questions


name = input("Enter your name: ")


def ask_question():
    if random.choice([True, False]):
        return questions.generate_square_question()
    return questions.generate_square_root_question()


score = 0


while True:
    question, answer = ask_question()
    start = datetime.now().timestamp()
    user_input = input(question)
    end = datetime.now().timestamp()
    if exceptions.check_error(user_input):
        continue
    if answer == int(user_input):
        score += 10
    else:
        score -= 5

    if score == 50:
        print("Great going! ")

    print(f"Score is: ", score)
    print("Time taken: ", round(end - start, 2), "s")
    choice = input("Do you want to continue the quiz? ")
    if choice != "yes":
        if score >= 100:
            print("You are a winner")

        else:
            print(f"{name} is a looser! Shame on you")
        break

