# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    i = l
    value = a[l]
    while i<=r:
        if a[i]==value:
            i +=1
        elif a[i]<value:
            a[i],a[l] = a[l],a[i]
            i+=1
            l+=1
        else:
            a[i],a[r] = a[r],a[i]
            r-=1
    return l,r
    

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1,m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
