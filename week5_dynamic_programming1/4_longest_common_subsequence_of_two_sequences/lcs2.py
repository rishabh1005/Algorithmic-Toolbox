#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    d = [[0]*(len(b)+1) for _ in range(len(a)+1)]

    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i==0 or j==0:
                d[i][j] = 0
            elif a[i-1]==b[j-1]:
                d[i][j] = d[i-1][j-1]+1
            else:
                d[i][j] = max(d[i-1][j],d[i][j-1])
    return d[len(a)][len(b)]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
