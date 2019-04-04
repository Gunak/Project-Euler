# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def pythagorean_triplet(a, b, c):
	 if (a < b < c) and (a + b + c == 1000):
	 	square1 = a**2 + b**2
	 	square2 = c**2
	 	if square1 == square2:
	 		return a*b*c
	 else:
	 	return None


for a in range(1,1001):
	for b in range(1,1001):
		for c in range(1, 1001):
			x = pythagorean_triplet(a,b,c)
			if x != None:
				print(x)