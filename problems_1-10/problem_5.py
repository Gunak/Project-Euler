# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def divisible_1_to_20(number):
	works = True
	for i in range(1, 21):
		# print(number % i)
		if number % i != 0:
			works = False
			return False
	return number


counter = 2520
while True:
	x = divisible_1_to_20(counter)
	# print(x is False)
	if x is False:
		counter +=1
	else:
		break

print(counter)