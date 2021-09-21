import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def creating_random_progression():
    """"Returns random progression."""

    length_pr = random.randint(8, 10)
    step_pr = random.randint(1, 10)
    first_pr = random.randint(0, 30)
    finish_pr = first_pr + length_pr * step_pr
    return [c for c in range(first_pr, finish_pr, step_pr)]


def selecting_list_item(progression):
    """Returns a hidden random element. \n
     Replacing it in the progression with '..'"""
    num_hidden_item = random.randint(1, (len(progression) - 1))
    hidden_item = str(progression[num_hidden_item])
    progression[num_hidden_item] = '..'
    return hidden_item, progression


def generate_round():
    progression = creating_random_progression()
    hidden_item, progression_hidden_item = selecting_list_item(progression)
    return progression_hidden_item, hidden_item
