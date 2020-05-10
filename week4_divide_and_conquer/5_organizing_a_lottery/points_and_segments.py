# Uses python3
import sys
from itertools import chain

def fast_count_segments(starts, ends, points,n,m):
    cnt = [0] * len(points)
    #write your code here
    '''lst = [(i,'s') for i in starts]+[(i,'e') for i in ends]+[(i,'p') for i in points]
    lst.sort()
    seg = 0
    for i in lst:
        if i[1] == 's':
            seg += 1
        elif i[1] == 'e':
            seg -= 1
        else:
            cnt[points.index(i[0])] = seg
    return cnt'''

    a,b,c = zip(starts,['l']*n,range(n)),zip(ends,['r']*n,range(n)),zip(points,['p']*m,range(m))

    lst = sorted(chain(a,b,c),key = lambda x : (x[0],x[1]))
    seg = 0
    for i,j,k in lst:
        if j=='l': seg+=1
        elif j=='r': seg-=1
        else: cnt[k] = seg
    return cnt



def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points,n,m)
    for x in cnt:
        print(x, end=' ')
