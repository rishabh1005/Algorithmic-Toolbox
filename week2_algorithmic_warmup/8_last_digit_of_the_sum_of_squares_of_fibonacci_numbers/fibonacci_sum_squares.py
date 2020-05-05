# Uses python3
from sys import stdin

'''def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10'''
    
def get_fibo(n):
    a,b = 0,1
    for _ in range(n-1):
        a,b=b,(a+b)%10

    return b

def fibonacci_sum_squares_fast(n):
    n %= 60
    if n<=0:
        return n
    else:
        return (get_fibo(n)*get_fibo(n+1))%10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_fast(n))
