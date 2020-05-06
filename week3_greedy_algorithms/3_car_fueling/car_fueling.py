# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    n = len(stops)
    stops = [0]+stops+[distance]
    numrefills, currentrefill = 0, 0
    while currentrefill <= n:
        lastrefill = currentrefill
        while currentrefill <= n and (stops[currentrefill+1]-stops[lastrefill]<=tank):
            currentrefill += 1
        if currentrefill==lastrefill:
            return -1
        if currentrefill<=n:
            numrefills+=1
    return numrefills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
