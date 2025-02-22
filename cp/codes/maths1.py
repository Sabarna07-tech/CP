def find_triangle_sides(t, test_cases):
    results = []
    for case in test_cases:
        a, b, c, d = case
        x = b
        y = c
        z = c
        results.append((x, y, z))
    return results

# Input reading
t = int(input())
test_cases = []
for _ in range(t):
    a, b, c, d = map(int, input().split())
    test_cases.append((a, b, c, d))

# Solve
results = find_triangle_sides(t, test_cases)

# Output
for res in results:
    print(res[0], res[1], res[2])