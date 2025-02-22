n = int(input())
if n % 2 == 0:
    print("NO SOLUTION")
else:
    perm = [1] * (n+1)
    perm[1] = 1
    perm[n] = n
    for i in range(2, n, 2):
        perm[i] = i+1
        perm[i+1] = i
    print(*perm[1:])