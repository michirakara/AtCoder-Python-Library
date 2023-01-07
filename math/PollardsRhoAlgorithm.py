def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def rho_algorithm(n, a=1, x0):
    f = lambda x: (x * x + a) % n
    x = y = ys = x0
    r = 1
    q = 1
    m = 100
    d = 1
    while d == 1:
        x = y
        for i in range(r):
            y = f(y)
        for k in range(0, r, m):
            ys = y
            for i in range(min(m, r - k)):
                y = f(y)
                q = q * abs(x - y) % n
            d = GCD(n, q)
            if d != 1:
                break
        r <<= 1
    if d == n:
        while d == 1:
            ys = f(ys)
            d = GCD(abs(x - ys), n)
    if d == n:
        return -1
    else:
        return d
