# x = g(x)
# |g(x) - g(y)| <= q|x - y|  0<q<1
# xn1 = g(xn)

# g(x) = x - f(x) / alpha
# 1) abs(alpha) > 1/2 max|(df(x)|     2) sgn(alpha) = sgn(df(x))     sgn(df(x))=constant on [a, b]

def g(x):
    return 3.0 - abs(x) / 2.0


def simple(g, x0, epsilon=1e-6):
    count = 1
    xn = x0
    xn1 = g(xn)
    while abs(xn1 - xn) > epsilon:
        count += 1
        xn = xn1
        xn1 = g(xn)

    return xn1, count


print(simple(g, 106))
