def f(x):
    print("If x ", x, " fx: ", x ** 3 + 4 * x ** 2 - 10)
    return x ** 3 + 4 * x ** 2 - 10


def bisection(f, a, b, epsilon=1e-5):
    count = 1
    c = a + ((b - a) / 2)
    while abs(f(c)) > epsilon:
        count += 1
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
        c = a + ((b - a) / 2)

    return c, count


print(bisection(f, 1, 2))
