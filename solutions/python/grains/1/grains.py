def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
    return (2 ** (number-1))
    
def total():
    total_grains = 0
    squares = 1
    while squares <= 64:
        total_grains = total_grains + (square(squares))
        squares +=1
    return total_grains
