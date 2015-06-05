# programming challenge @ http://developersleague.net/programming-challenge-1/
from math import factorial
def results(a,b):
	if a < 25 and b < 25:
		return 0
	elif a == 25:
		return  factorial(24+b)/(factorial(b) * factorial(24))
	elif b == 25:
		return  factorial(24+a)/(factorial(a) * factorial(24))
	elif a == b + 2 and b > 23:
		return (factorial(48)/(factorial(24)* factorial(48 - 24))) * (2 ** b - 24) % (10 ** 9)
	elif b == a + 2 and a > 23:
		return (factorial(48)/(factorial(24)* factorial(48 - 24))) * (2 ** a - 24) % (10 ** 9)

# test case 1
print(results(3,25))

# test case 2
print(results(24,17))

# test case 3
print(results(10**9, (10**9)-2))