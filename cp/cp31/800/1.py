def main():
    t = int(input().strip())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        # Create a sorted copy of the original list.
        copy_a = sorted(a)
        if copy_a == a or k > 1:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()