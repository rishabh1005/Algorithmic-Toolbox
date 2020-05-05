# Uses python3
import sys
import math
def lcm_naive(a, b):
    
    return int(a*b/math.gcd(a,b))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

