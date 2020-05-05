# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    n = n%60
    if n==0:
        return 0
    if n==1:
        return 1
    a,b = 0,1
    for i in range(2,n+1):
        c = (a+b)%10
        a,b = b,c
    return c

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
