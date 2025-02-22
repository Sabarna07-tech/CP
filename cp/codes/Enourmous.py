import os
import  sys


def divisible(t,k):
    count = 0 
    for i in range(len(t)):
        if t[i] % k == 0:
            count = count+1
            return count
def main():
    n,k = map(int, sys.stdin.readline().split())
    for _ in range(n):
        M = 10^9
        t = list(map(int, os.read(0, M).split()))
        result = divisible(t,k)
        print(result)
if __name__ == "__main__":
    main()       
        
    