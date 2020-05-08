#Uses python3

import sys

def bestdigit(max_number,x):
    return int(max_number+x)<=int(x+max_number)

def largest_number(a):
    #write your code here
    res = []
    while a != []:
        max_number = 0
        for x in a:
            if bestdigit(str(max_number),str(x)):
                max_number = x
        res.append(max_number)
        a.remove(max_number)
    a = "".join([str(i) for i in res])
    return a

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
