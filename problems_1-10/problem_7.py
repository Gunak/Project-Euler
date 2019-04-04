# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10,001st prime number?


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



counter = 0
primes_found = 0

while primes_found < 10001:
	counter += 1
	x = prime_number(counter)
	# print(x)
	if x != False:
		primes_found += 1

print(prime_number(counter))