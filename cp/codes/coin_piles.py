def coin(a,b):
    if (2*a-b)%3 != 0 or (2*a - b)%3 < 0 or (2*b-a)%3 != 0 or (2*b -a)%3 < 0 :
        return 'NO\n'
    return 'YES\n'
        
if __name__ == '__main__':
    t = int(input())
    queries = []
    for _ in range(t):
        a, b = map(int, input().split())
        queries.append((a, b))

    for query in queries:
        a, b = query
        print(coin(a, b), end="")