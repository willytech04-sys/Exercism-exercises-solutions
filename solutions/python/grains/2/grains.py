"""Function for calculating grains of wheat on a chessboard."""
def square(number):
    """Return the number of grains on a given square."""
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number-1)
    
def total():
    """Return the total number of grains on the chessboard."""
    total_grains = 0
    squares = 1
    while squares <= 64:
        total_grains = total_grains + square(squares)
        squares +=1
    return total_grains
