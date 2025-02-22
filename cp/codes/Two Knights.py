def two_knights(K):
    # Total number of ways two knights can be placed on
    # the chessboard
    total_ways = ((K * K) * ((K * K) - 1)) // 2

    # Number of ways two knights can attack each other
    attacking_ways = 4 * (K - 1) * (K - 2)

    # Number of ways two knights can be placed without
    # attacking each other
    ans = total_ways - attacking_ways

    # Return the result for the current chessboard size
    return ans

# Driver Code
def main():
    # Input the value of N (size of the chessboard)
    N = int(input())

    # Iterate for all the K sized chessboard
    for K in range(1, N + 1):
        print(two_knights(K), end=" ")

if __name__ == "__main__":
    main()