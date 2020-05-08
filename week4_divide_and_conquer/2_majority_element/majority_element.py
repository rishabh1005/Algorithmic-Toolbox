# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    mid  = (right+left-1)//2+1
    left_value = get_majority_element(a,left,mid)
    right_value = get_majority_element(a,mid,right)
    l,r = 0,0
    for i in a[left:right]:
        if i == left_value:
            l += 1
        elif i == right_value:
            r += 1
    if (right - left)//2<l :
        return left_value
    elif (right - left)//2<r :
        return right_value
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
