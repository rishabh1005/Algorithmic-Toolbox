# Uses python3
import sys

def get_change(mn):
    #write your code here
    minnumcoins = [0]*(mn+1)
    coins=[1,3,4]
    for m in range(1,mn+1):
        minnumcoins[m] = 10**18
        for i in coins:
            if m>=i:
                numcoin = minnumcoins[m-i]+1
                minnumcoins[m] = min(numcoin,minnumcoins[m])
    return minnumcoins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
