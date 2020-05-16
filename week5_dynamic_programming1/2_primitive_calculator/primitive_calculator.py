# Uses python3
import sys

def optimal_sequence(n):
    num = solution(n)
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0 and (num[n//3]==num[n]-1):
            n = n // 3
        elif n % 2 == 0 and (num[n//2]==num[n]-1):
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def solution(n):

    num = [0]*(n+1)
    for i in range(1,n+1):
        num[i] = num[i-1]+1
        if i%2==0:
            num[i] = min(num[i//2]+1,num[i])
        if i%3==0:
            num[i] = min(num[i//3]+1,num[i])
    return num


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence)-1)
for x in sequence:
    print(x, end=' ')
