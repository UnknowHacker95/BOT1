def a(x):
    a = 3 * x - 112
    b = 3 * x + 58
    while (a != b):
        if (a > b):
            a -= b
        else:
            b -= a
    return a


for i in range(1, 100):
    k = a(i)
    if (k == 34):
        print(i)
print("!")