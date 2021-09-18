import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd_rem_division(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


def generate_round():
    """Function defines conditions of the brain-calc game."""

    first_random_number = random.randint(1, 10)
    second_random_number = random.randint(1, 10)
    question = '{0} {1}'.format(first_random_number, second_random_number)
    correct_answer = str(gcd_rem_division(first_random_number,
                                          second_random_number))
    return question, correct_answer
