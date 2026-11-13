"""Determine whether a number is an Armstrong number."""
def is_armstrong_number(number):
    """Returns true if a number is an Armstrong number and false if not"""
    total = 0
    count = len(str(number))
    for num in str(number):
        total += int(num) ** count
    return total == number
    
