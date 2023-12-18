# g(x) = x - f(x) / df(x)

def f(x):
    return x ** 3 + 4 * x ** 2 - 10


def df(x):
    return 3 * x ** 2 + 8 * x


def newton(f, df, x0, epsilon=1e-6):
    count = 1
    xn = x0
    xn1 = xn - f(xn) / df(xn)
    while abs(xn1 - xn) > epsilon:
        count += 1
        xn = xn1
        xn1 = xn - f(xn) / df(xn)

    return xn1, count


print(newton(f, df, 1.7))
