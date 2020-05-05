# Uses python3
import sys

'''def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m'''

def fib_period_of_cycle(m):

    if n<=1:
        return n
    
    a,b = 0,1
    for i in range((m*m)+1):
        a,b = b,(a+b)%m
        if a==0 and b==1:
            return i+1

def get_fibonacci_huge_fast(n,m):
    if n<=1:
        return n
    rem=n%fib_period_of_cycle(m)
    if rem<=1:
        return rem
    a,b = 0,1
    for _ in range(rem-1):
        a,b=b,(a+b)

    return b%m


if __name__ == '__main__':
    #input = sys.stdin.read();
    n, m = map(int, input().split())
    print(get_fibonacci_huge_fast(n, m))
