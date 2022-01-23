
EXPECTED_BAKE_TIME = int(40)
PREPARATION_TIME = int(2)
elapsed_bake_time = 30
number_of_layers = 4

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.
    
    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.
    
    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    bake_time = EXPECTED_BAKE_TIME - int(elapsed_bake_time)
    return(int(bake_time))

print('The time remaining is', bake_time_remaining(elapsed_bake_time), 'minutes.')


# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(number_of_layers):
    prep_time = int(number_of_layers) * PREPARATION_TIME
    return(int(prep_time))

print('The amount of prep time for', number_of_layers, 'layers is', preparation_time_in_minutes(number_of_layers), 'minutes.')

# TODO: define the 'elapsed_time_in_minutes()' function
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    elasped_time = preparation_time_in_minutes(number_of_layers) + int(elapsed_bake_time)
    return(elasped_time)

print('The total amount of time passed since making the lasagna is', elapsed_time_in_minutes(number_of_layers, elapsed_bake_time))