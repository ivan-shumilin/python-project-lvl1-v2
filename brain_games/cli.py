"""Function welcom_user."""

import prompt


def welcome_user():
    """Print welcome."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))  # Noqa:WPS421
