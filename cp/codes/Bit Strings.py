def bit_string(n):
    M = 1000000007
    if n>0:
        print(2**n % M)



if __name__ == "__main__":
    n = int(input())
    bit_string(n)