# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(M, m, i, j, op):
    min_value = 10**18
    max_value = -10**18
    for k in range(i, j):
        a = evalt(M[i][k], M[k+1][j], op[k])
        b = evalt(M[i][k], m[k+1][j], op[k])
        c = evalt(m[i][k], M[k+1][j], op[k])
        d = evalt(m[i][k], m[k+1][j], op[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value

def get_maximum_value(num ,op):
    #write your code here
    n = len(num)
    m = [[0]*n for x in range(n)]
    M = [[0]*n for x in range(n)]

    for i in range(n):
        m[i][i] = num[i]
        M[i][i] = num[i]

    for s in range(1, n):
        for i in range(0, n-s):
            j = i + s
            m[i][j], M[i][j] = MinAndMax(M, m, i, j, op)

    return M[0][n-1]

if __name__ == "__main__":
    exp = input()
    num,op = [],[]
    for i in exp :
        if i in ['+', '-', '*']:
            op.append(i)
        else:
            num.append(int(i))
    print(get_maximum_value(num,op))
