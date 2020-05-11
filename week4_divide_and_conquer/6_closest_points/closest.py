#Uses python3
import sys
import math

def distance(p1,p2):
    return math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))

def bruteforce(point):
    min=distance(point[0],point[1])
    p1,p2,len_point = point[0],point[1],len(point)
    if len_point ==2:
        return p1,p2,min
    for i in range(len_point-1):
        for j in range(i+1,len_point):
            if i!=0 and j!=1 :
                d = distance(point[i],point[j])
                if d<min: p1,p2,min=point[i],point[j],d
    return p1,p2,min

def nearlineclosestpair(xsort,ysort,d,best):
    n = len(xsort)
    mid_x = xsort[n//2][0]

    s = []
    for i in ysort:
        if mid_x - d <= i[0] <= mid_x+d:
            s.append(i)

    len_s = len(s)
    for i in range(len_s-1):
        for j in range(i+1,min(i+6,len_s)):
            p,q = s[i],s[j]
            new_d = distance(p,q)
            if new_d<d:
                d = new_d
                best = p,q
    return best[0],best[1],d

def closestpair(xsort,ysort):
    n = len(xsort)
    if n<=3:
        return bruteforce(xsort)
    mid = n//2
    midpoint = xsort[mid][0]
    l_x = xsort[:mid]
    r_x = xsort[mid:]
    l_y,r_y=[],[]
    for x in ysort:
        if x[0]<=midpoint:
            l_y.append(x)
        else:
            r_y.append(x)

    p1,q1,m1 = closestpair(l_x,l_y)
    p2,q2,m2 = closestpair(r_x,r_y)

    if m1<=m2:
        d = m1
        point = (p1,q1)
    else:
        d = m2
        point = (p2,q2)

    p,q,m = nearlineclosestpair(xsort,ysort,d,point)

    if d<=m:
        return point[0],point[1],d
    else:
        return p,q,m


def minimum_distance(x, y):
    #write your code here
    point = list(zip(x,y))
    xsort = sorted(point,key = lambda x:x[0])
    ysort = sorted(point,key = lambda x:x[1])
    p1,p2,min = closestpair(xsort,ysort)

    return min

if __name__ == '__main__':
    '''input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]'''
    x=[]
    y=[]
    for _ in range(int(input())):
        x_value,y_value = map(int,input().split())
        x.append(x_value)
        y.append(y_value)
    print("{0:.4f}".format(minimum_distance(x, y)))

