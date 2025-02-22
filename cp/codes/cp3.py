import sys

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ans = a[0]
    for i in range(n):
        if i % 2 == 0:
            ans = max(ans, a[i])

    print(ans)
        