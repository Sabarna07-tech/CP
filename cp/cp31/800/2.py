# A. Line Trip
def main():
    t = int(input().strip())
    for _ in range(t):
        n, x = map(int, input().split())
        points_arr = [0]
        # Read n points
        points = list(map(int, input().split()))
        points_arr.extend(points)
        points_arr.append(x)
        
        max_distance = float('-inf')
        for i in range(1, len(points_arr)):
            if i == len(points_arr) - 1:  # Last segment
                diff = 2 * (points_arr[i] - points_arr[i - 1])
            else:
                diff = points_arr[i] - points_arr[i - 1]
            max_distance = max(max_distance, diff)
        print(max_distance)

if __name__ == "__main__":
    main()