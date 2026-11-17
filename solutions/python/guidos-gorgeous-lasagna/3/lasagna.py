"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""




EXPECTED_BAKE_TIME= 40 
def bake_time_remaining(timeElapsed):
    """Calculate remaining bake time in minutes.
    
    Parameters:
         timeElapsed(int): The actual minutes the lasagna has been in the oven.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the actual minutes the lasagna has been in the oven and the expected bake time of     the lasagna. It calculates 
    the total remaining time in minutes (EXPECTED_TIME - timeElapsed).
    
    """   
    remaining_time=EXPECTED_BAKE_TIME - timeElapsed
    return remaining_time

def preparation_time_in_minutes(number_of_layers):   
    """Calculate the elapsed preparation time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        
    
    Returns:
        int: The total time elapsed (in minutes) preparing.

    This function takes  an integer representing the number of lasagna 
    layers. It calculates 
    the total elapsed minutes spent preparing.
    
    """   
    PREPARATION_TIME = number_of_layers * 2
    return PREPARATION_TIME

def elapsed_time_in_minutes(numbers_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """    
    numbers_of_layers *=2
    return numbers_of_layers + elapsed_bake_time



    

