# Problem 1 - Multiples of 3 and 5
#  https://projecteuler.net/problem=1

# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


def sum(aList):
    total = 0
    for n in aList:
        total += n
    print(total)

def create_list(start, stop):
    aList = []
    for x in range(start, (stop)):
        if x % 5 == 0 or x % 3 == 0:
            aList.append(x)
    return aList
        

if __name__ == "__main__":
    x = create_list(1,1000)
    y = sum(x)


# Answer: 233168
