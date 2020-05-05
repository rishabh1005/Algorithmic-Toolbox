# Uses python3
import sys

'''def fibonacci_partial_sum_naive(from_, to):
    if from_==0 and to==0:
        return 0
    if from_==0 and to==0:
        return 1
    a,b = 0,1
    c=0
    for i in range(2,to+3):
        c = (a+b)%10
        a,b = b,c
    c-=1

    a,b = 0,1
    s=0
    for i in range(2,from_+1):
        s = (a+b)%10
        a,b = b,s

    return c-s'''

def get_fibo(n):
    if n<=1:
        return n
    rem=n%60
    a,b = 0,1
    for _ in range(rem-1):
        a,b=b,(a+b)

    return b%10
    
def fibonacci_partial_sum_fast(from_, to):
    if from_ == to:
        return get_fibo(from_%60)
    else:
        from_ %=60
        to %=60
        from_last = get_fibo(from_+1)-1
        to_last = get_fibo(to+2)-1

    return (to_last-from_last)%10



if __name__ == '__main__':
    #input = sys.stdin.read();
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_fast(from_, to))