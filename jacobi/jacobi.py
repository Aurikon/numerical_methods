def summator(A, b, x):
    n = len(x)
    res = [0] * n
    for i in range(n):
        s = 0
        for j in range(n):
            if i == j:
                continue
            s += A[i][j] * x[j]

        res[i] = -(s + b[i]) / A[i][i]

    return res


def norm(x1, x2):
    return max(abs(x1[i] - x2[i]) for i in range(0, len(x1)))


def jacobi(A, b, epsilon=1e-6):
    count = 1
    n = len(b)
    xk = [0] * n
    xk1 = summator(A, b, xk)
    while norm(xk1, xk) > epsilon:
        count += 1
        xk = xk1
        xk1 = summator(A, b, xk)

    return xk1, count


A = [[2, -1, 0], [1, 6, -2], [4, -3, 8]]
b = [2, -4, 5]
print(jacobi(A, b))
