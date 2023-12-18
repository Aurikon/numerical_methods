def norm(x1, x2):
    return max(abs(x1[i] - x2[i]) for i in range(0, len(x1)))


def summator(A, b, xk, xk1):
    xk1 = xk1.copy()
    n = len(xk)
    for i in range(0, n):
        s1 = 0
        s2 = 0
        for j in range(0, i):
            s1 += A[i][j] * xk1[j]
        for j in range(i + 1, n):
            s2 += A[i][j] * xk[j]

        xk1[i] = (-s1 - s2 + b[i]) / A[i][i]

    return xk1


def gauss_seidel(A, b, epsilon=1e-6):
    count = 1
    n = len(b)
    xk = [0] * n
    xk1 = summator(A, b, xk, xk)

    while norm(xk, xk1) > epsilon:
        count += 1
        xk = xk1
        xk1 = summator(A, b, xk, xk1)

    return xk1, count


A = [[2, -1, 0], [1, 6, -2], [4, -3, 8]]
b = [2, -4, 5]
print(gauss_seidel(A, b))
