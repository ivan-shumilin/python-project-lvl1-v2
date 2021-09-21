import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    divisor = 2
    while number % divisor != 0:
        divisor += 1
    return divisor == number


def generate_round():
    question = random.randint(1, 100)
    correst_answer = 'yes' if is_prime(question) else 'no'
    return question, correst_answer
