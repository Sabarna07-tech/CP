# B. Chemistry
def solve():
    import sys
    input = sys.stdin.readline
    t = int(input().strip())
    results = []
    for _ in range(t):
        n, k = map(int, input().split())
        s = input().strip()
        
        
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        
        odd_count = sum(1 for f in freq if f % 2 == 1)

        remaining = n - k
        required_odd = remaining % 2

        diff = abs(odd_count - required_odd)
        
        if k >= diff and (k - diff) % 2 == 0:
            results.append("YES")
        else:
            results.append("NO")
    
    sys.stdout.write("\n".join(results))


if __name__ == '__main__':
    solve()
