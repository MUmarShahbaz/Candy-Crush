import structs as s
import random


# Misc Functions
def no_candy(candy : s.Candy):
    return candy.color == s.COLOR.N and candy.mode == s.MODE.N

def candy_is_special(candy : s.Candy):
    return not no_candy(candy) and candy.mode != s.MODE.N

def random_candy() -> s.Candy:
    new_candy = s.Candy()
    new_candy.color = random.choice([s.COLOR.RED, s.COLOR.ORANGE, s.COLOR.YELLOW, s.COLOR.GREEN, s.COLOR.BLUE, s.COLOR.PURPLE])
    new_candy.mode = s.MODE.N
    return new_candy