# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def largest_palindrome(smallest, largest):
	palindrome = []
	largest_number = []
	for i in range(largest, smallest, -1):
		for j in range(largest, smallest, -1):
			num = i * j
			num = str(num)
			if num == num[::-1]:
				palindrome.append(int(num))

	for k in palindrome:
		if len(largest_number) > 0:
			if largest_number[0] < k:
				largest_number[0] = k
			else:
				pass
		else:
			largest_number.append(k)

	return largest_number[0]


x = largest_palindrome(100, 999)
print(x)
