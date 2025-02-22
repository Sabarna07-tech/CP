MOD = 10**9 + 7

def compute_stirling_numbers(n):
    S = [[0] * (n + 1) for _ in range(n + 1)]
    S[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            S[i][j] = (j * S[i - 1][j] + S[i - 1][j - 1]) % MOD
            
    return S

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    Q = int(data[0])
    index = 1
    results = []
    
    max_n = 0
    queries = []
    for _ in range(Q):
        N = int(data[index])
        max_n = max(max_n, N)
        parents = list(map(int, data[index + 1:index + N]))
        index += N
        queries.append((N, parents))
    
    stirling = compute_stirling_numbers(max_n)
    
    for N, parents in queries:
        if N == 1:
            results.append(1)
            continue
        
        is_leaf = [True] * (N + 1)
        is_leaf[1] = False  # Root is never a leaf
        for parent in parents:
            is_leaf[parent] = False
        
        leaf_count = sum(is_leaf[1:])
        
        results.append(stirling[N][leaf_count])
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")

