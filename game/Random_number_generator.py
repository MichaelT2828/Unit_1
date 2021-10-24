def rng(first:int, second:int): # so def is basically just a small section of code that you know you will reuse
    # rng is just the name of the function, the stuff inside the () is the arguments you will plug into the function
    from random import randint
    value = randint(first, second)
    return value
