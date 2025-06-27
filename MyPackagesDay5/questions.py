import random

def generate_square_question():
    num = random.randint(1, 100)
    question = f'What is the square of {num}? '
    answer = num**2
    return question, answer


def generate_square_root_question():
    root = random.randint(1, 100)
    question = f'What is the square root of {root ** 2}? '
    answer = root
    return question, answer