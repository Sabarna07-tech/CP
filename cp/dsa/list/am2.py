def f(dp, n, k):
    if n == 1:
        return 1 if k == 1 else 0

    if dp[n][k] != -1:
        return dp[n][k]

    ways = 0
    if k > 1:
        ways += f(dp, n - 1, k - 1)
    if k < n:
        ways += f(dp, n - 1, k)

    dp[n][k] = ways
    return dp[n][k]

def lastElement(input1, input2):
    n = input1
    k = input2
    dp = [[-1 for _ in range(k + 1)] for _ in range(n + 1)]
    return f(dp, n, k)

#Example usage
input1 = 5
input2 = 3
print(lastElement(input1, input2))


