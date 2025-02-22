def main():
    t = int(input().strip())
    for _ in range(t):
        n= int(input().strip())
        s = input().strip()
        ans = n
        left = 0, right = 0
        while(left<=right):
            if(s[left] != s[right]):
                ans -= 2
            else:
                break
            left += 1
            right -= 1
        print(ans)
if __name__ == "__main__":
    main()
            