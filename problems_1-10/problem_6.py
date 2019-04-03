# The sum of the squares of the first ten natural numbers is,

# 1**2 + 2**2 + ... + 10**2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)**2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def square_each(numbers):
	total = 0
	for i in numbers:
		total += i**2
	return total

def square_total(numbers):
	total = 0
	for i in numbers:
		total += i

	return total**2





total1 = square_each(range(1,101))
total2 = square_total(range(1,101))



print(total2-total1)