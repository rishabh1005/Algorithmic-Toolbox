# Uses python3
import sys
import itertools

def partition3(A):
    W = 0 if sum(A)%3!=0 else sum(A)//3
    if len(A)<3 or W==0:
        return 0
    else:
        count = 0
        weights  = [[0]*(len(A)+1) for _ in range(W+1)]
        for i in range(1,W+1):
            for j in range(1,len(A)+1):
                weights[i][j] = weights[i][j-1]
                if A[j-1]<=i:
                    temp = weights[i-A[j-1]][j-1] + A[j-1]
                    if temp>weights[i][j] : weights[i][j] = temp
                if weights[i][j] == W: count+=1

        if count<3: return 0
        else: return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

