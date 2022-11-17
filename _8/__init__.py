def maximal(a, b):
    if a >= b:
        return [a, b]
    return [b, a]

[mayor, menor] = maximal(int(input("a: ")), int(input("b: ")))

if mayor % menor == 0:
    print("Si")
else:
    print("No")