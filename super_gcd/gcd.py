def gcd(x, y):
    for i in range(min(x, y), 0, -1):
        if y % i == 0 and x % i == 0:
            return i
