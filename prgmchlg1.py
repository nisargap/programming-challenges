from math import factorial
def results(a,b):
	if a < 25 and b < 25:
		return factorial(a+b)/(factorial(b) * factorial(a))
	elif a == 25:
		return  factorial(24+b)/(factorial(b) * factorial(24))
	elif b == 25:
		return  factorial(24+a)/(factorial(a) * factorial(24))
	elif a == b + 2 and b > 23:
		return (factorial(48)/(factorial(24)* factorial(48 - 24))) * (2 ** b - 24)
print(results(3,25))