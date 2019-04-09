# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


def prime_number(number):
	if number == 1:
		return False
	elif number == 2:
		return number
	elif number % 2 == 0:
		return False
	else:
		for i in range(3, number, 2):
			# print(f'\t {i}')
			if number % i == 0 or i > number:
				return False
		else:
			return number


total = 0
for i in range(1,10, 2):
	print(i)
	x = prime_number(i)
	total += x

	
	# if x != False:
	# 	print(x)
	# 	total += x

print(total)