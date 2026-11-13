"""Function to calculate the points scored in a single toss of a Darts game."""
import math
def score(x, y):
    distance = math.sqrt(x**2 + y**2)
    if distance > 10:
        return 0
    if 5 < distance <= 10:
        return 1
    if 1 < distance <= 5:
        return 5
    else:
        if 0 <= distance <=1:
            return 10
    