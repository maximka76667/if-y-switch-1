a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))


def minimal(numbers):
    numMin = float('inf')
    for i in range(0, len(numbers), 1):
        num = numbers[i]
        if num < numMin:
            numMin = num

    return numMin


print(minimal([a, b, c]))
