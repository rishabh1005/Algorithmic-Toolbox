# Uses python3
def calc_fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    a = [0,1]
    for i in range(2,n+1):
        a.append(a[i-1]+a[i-2])
    return a[-1]

n = int(input())
print(calc_fib(n))
