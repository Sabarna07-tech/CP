def count_ways(n):
    MOD = 10**9 + 7
    dp = [0] * (n + 1)
    dp[0] = 1  

    for i in range(1, n + 1):
        for dice in range(1, 7):
            if i - dice >= 0:
                dp[i] = (dp[i] + dp[i - dice]) % MOD

    return dp[n]
def main():
    N = int(input())
    print(count_ways(N))

if __name__ == "__main__":
    main()
