"""
Calculator library containing basic math operations.
"""


def add(first_term, second_term):
    return first_term + second_term


def subtract(first_term, second_term):
    return first_term - second_term

def sqr(value):
    return value*value

def fac(value):
    # @TODO: Implement Faculty
    if value < 0:
        print(f"ValueError: value ({value}) should be positiv")
        raise ValueError(f"ValueError: value ({value}) should be positiv")
    elif value < 2:
        return value
    else:
        return value * fac(value - 1)
