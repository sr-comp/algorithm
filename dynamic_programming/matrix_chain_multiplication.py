def optimal_matrix_chain(p, m, s):
    n = len(p) - 1
    for i in range(0, n):
        m.append([])
        s.append([])
        for j in range(0, n):
            m[i].append([])
            s[i].append([])
    for i in range(0, n):
        m[i][i] = 0
    for l in range(2, n + 1):
        for i in range(0, n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                tmp = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j]
                if m[i][j] > tmp:
                    m[i][j] = tmp
                    s[i][j] = k


def print_optimal_matrix_chain(s, i, j):
    if i == j:
        print("A" + str(i), end="")
    else:
        print("(", end="")
        print_optimal_matrix_chain(s, i, s[i][j])
        print(")*(", end="")
        print_optimal_matrix_chain(s, s[i][j] + 1, j)
        print(")", end="")


if __name__ == '__main__':
    p = [30, 35, 15, 5, 10, 20, 25]
    m = []
    s = []
    optimal_matrix_chain(p, m, s)
    print(m[0][5])
    print(s[0][5])
    print_optimal_matrix_chain(s, 0, 5)