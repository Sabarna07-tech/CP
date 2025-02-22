def solve_cases(t, cases):
    results = []
    for case in cases:
        n, arr = case
        same_parity = True
        for i in range(n):
            if arr[i] % 2 != arr[0] % 2:
                same_parity = False
                break

        if not same_parity:
            results.append([-1])
            continue

        ansarr = []
        for _ in range(40):
            arr.sort()
            x = (arr[0] + arr[-1]) // 2
            ansarr.append(x)
            for j in range(n):
                arr[j] = abs(arr[j] - x)

        results.append([len(ansarr)] + ansarr)
    
    return results


t = int(input())
cases = []
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    cases.append((n, arr))


output = solve_cases(t, cases)
for res in output:
    if res[0] == -1:
        print(-1)
    else:
        print(res[0])
        print(" ".join(map(str, res[1:])))

