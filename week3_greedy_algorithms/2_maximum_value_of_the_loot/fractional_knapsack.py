# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    location = list(range(len(values)))
    d = [v/w for w,v in zip(weights,values)]
    location.sort(key = lambda x: d[x],reverse = True)
    for i in location:
        if weights[i]<=capacity:
            value += values[i]
            capacity -= weights[i]
        else:
            value += values[i]*capacity/weights[i]
            break
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
