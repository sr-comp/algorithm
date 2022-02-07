import random
import sys


def rod_cutting_recursive(n, p):
    if n == 0:
        return 0
    else:
        q = float('-inf')
        for i in range(1, n + 1):
            tmp = rod_cutting_recursive(n-i, p) + p[i]
            q = tmp if tmp > q else q
        return q


def rod_cutting_memoized(n, p, r):
    if n == 0 or r[n] > -1:
        return r[n]
    else:
        q = float('-inf')
        for i in range(1, n + 1):
            tmp = rod_cutting_memoized(n-i, p, r) + p[i]
            q = tmp if tmp > q else q
        r[n] = q
        return q


if __name__ == '__main__':
    p = random.sample(range(1, 2000), 1000)
    p[0] = 0
    p.sort()
    n = len(p) - 1
    r = []
    r.append(0)
    for i in range(1, n + 1):
        r.append(-1)
    # print(rod_cutting_recursive(n, p))
    sys.setrecursionlimit(1500)
    print(rod_cutting_memoized(n, p, r))
