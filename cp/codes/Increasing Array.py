# Function to find the minimum number of moves
def solve(arr, N):
    # variable to store the final answer
    ans = 0
    # Iterate over all the elements and compare them with
    # the previous element
    for i in range(1, N):
        if arr[i - 1] > arr[i]:
            ans += (arr[i - 1] - arr[i])
            arr[i] = arr[i - 1]
    return ans

def main():
    # Sample Input
    N = int(input())
    arr = list(map(int, input().split()))

    print(solve(arr, N))

if __name__ == "__main__":
    main()