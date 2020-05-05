# Uses python3
import sys



def fibonacci_sum(n):
    rem=n%60
    a,b = 0,1
    for _ in range(rem+1):
        a,b=b,(a+b)

    return (b-1)%10
    

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    print(fibonacci_sum(n))
    
    
