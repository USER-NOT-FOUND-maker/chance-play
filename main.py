from random import choice
import matplotlib.pyplot as mpl

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

		if not self.bias:
			self.bias = bias
		
		if len(bias) > self.sides:
			raise ValueError("you MUST pass a dictionary of a length less than the number of sides for this argument")
		
		total = 0

		for i in bias.values():
			total += i

		if total > 1 or total <= 0:
			raise ValueError("your dictionary can not have biases that sum up to something more than 1 or dont sum up to anything (i.e. sum up to 0 or less than 0")

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

		if bias[1] == 1:
		    self.sides = 1
		    self.LSides = [bias[0]]
		    return
		elif bias[1] == 0:
		    self.sides = 1
		    self.LSides.remove(bias[0])
		    return

		self.sides = ["H" for i in range(50)] + ["T" for i in range(50)]

		if round(bias[1],3) != bias[1]:
		    print(f"\n{'='*100}\nFOR PERFORMANCE REASONS, YOUR BIAS HAS BEEN ROUNDED TO 3 DECIMAL PLACES\n{'='*100}\n")
		    bias[1] = round(bias[1],3)
	    
		lenBias = len(str(bias[1])) - 2 # -2 to account for the 0. part
		power = 10**lenBias 
		bias[1] = int(bias[1] * power)
		
		print(bias[1])

		if bias[0] == "H":
		    otherSide = "T"
		else:
		    otherSide = "H"

		otherProb = 1*power - bias[1]
		
		print(otherProb)

		newList = [bias[0] for i in range(bias[1])] + [otherSide for i in range(otherProb)]
		self.sides = newList

		self.bias = bias

	def __str__(self):
		return f"this is a coin with bias {self.bias}\nthe list for this coin is {self.sides}\n"

	def roll(self):
		return choice(self.LSides)

coin = coin(bias=("H",1))

while coin.roll != "T":
	print(coin.roll())
