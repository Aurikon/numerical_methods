# df(x) = (f(xn) - f(xn_1)) /  (xn - xn_1)
# xn1 = xn - (f(xn) * (xn - xn_1)) / (f(xn) - f(xn_1))

def f(x):
    return x ** 3 + 4 * x ** 2 - 10


def secant(f, x0, x1, epsilon=1e-6):
    count = 1
    xn_1 = x0
    xn = x1
    xn1 = xn - (f(xn) * (xn - xn_1)) / (f(xn) - f(xn_1))
    while abs(f(xn1)) > epsilon:
        count += 1
        xn_1 = xn
        xn = xn1
        xn1 = xn - (f(xn) * (xn - xn_1)) / (f(xn) - f(xn_1))

    return xn1, count


print(secant(f, 2, 1.9999))
