"""Determine the Collatz Conjecture"""
def steps(number):
    """Returns the number of steps needed to reach 1"""
    count = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        if number % 2 == 0:
            result = number // 2
        else:
            result = number * 3 + 1
        count += 1
        number = result
    return count
