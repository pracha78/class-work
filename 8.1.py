number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def chop(number):
    del number[0]
    del number[-1]
    print (number)

print (chop(number))


def middle(number):
    t = number[1:-1]
    return t

print (middle(number))