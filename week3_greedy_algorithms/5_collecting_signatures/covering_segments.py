# Uses python3
import sys
from operator import attrgetter
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(n,segments):
    points = []
    #write your code here
    segments.sort(key = attrgetter('end'))
    max_end = segments[0].end
    i=1
    points.append(max_end)
    while i < n:
        if max_end < segments[i].start:
            max_end = segments[i].end
            points.append(max_end)
        i+=1
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(n,segments)
    print(len(points))
    print(*points)
