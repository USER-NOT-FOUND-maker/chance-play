import matplotlib as mpl
from random import choice

class InvalidSide(Exception):
    def __init__(self,msg):

        self.msg = msg

# biased die is a future feature i might want to introduce later, heres how it MIGHT work

"""
for the bias argument you pass in a dictionary following this structure

{number you want to have a bias to : the bias you want to have to that number (just the probability of getting that number)}

we would append the key to the list of sides in the dice an amount value times


"""

class dice:
    def __init__(self,sides,bias={}):
        self.sides = sides
        self.Lsides = [i for i in range(sides)]

class coin:
    def __init__(self,bias=0):
        self.sides = ["H","T"]

        if bias == 0:
            self.bias = "no bias"
            return
        
        bias = list(bias)

        if bias[0].upper() not in self.sides:
            raise InvalidSide("you passed in an incorrect value for what side of the coin should be biased, you can only pass in 'H' and 'T' (not case sensitive")
        
        if len(bias) != 2:
            raise ValueError("you MUST pass only 2 arguments for the bias, first argument is what side the bias is called to, the 2nd argument is the probability of getting that side")
        
        if bias[1] > 1 or bias[1] < 0:
            raise ValueError("probability must be between 0 and 1 (to get percentage probability, multiply your number by 100)")

        self.sides = ["H" for i in range(50)] + ["T" for i in range(50)]
        
        if round(bias[1],3) != bias[1]:
            print(f"\n{'='*100}\nFOR PERFORMANCE REASONS, YOUR BIAS HAS BEEN ROUNDED TO 3 DECIMAL PLACES\n{'='*100}\n")
            bias[1] = round(bias[1],3)
        
        lenBias = len(str(bias[1])) - 2 # -2 to account for the 0. part
        power = 10**lenBias 
        bias[1] = int(bias[1] * power)

        if bias[0] == "H":
            otherSide = "T"
        else:
            otherSide = "H"
        
        otherProb = 1*power - bias[1]

        newList = [bias[0] for i in range(bias[1])] + [otherSide for i in range(otherProb)]
        self.sides = newList
        
        self.bias = bias

    def __str__(self):
        return f"this is a coin with bias {self.bias}\nthe list for this coin is {self.sides}\n"
    
    def roll(self):
        return choice(self.sides)

