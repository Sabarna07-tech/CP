def is_leaf_cactus(n, m, edges):
    from collections import defaultdict, deque

    graph = defaultdict(list)
    degree = [0] * (n + 1)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    def bfs(start):
        queue = deque([start])
        visited = [False] * (n + 1)
        visited[start] = True
        cycles = 0

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                elif degree[neighbor] > 2:  # Detect if it's a part of more than one cycle
                    cycles += 1

        return cycles

    for i in range(1, n + 1):
        if degree[i] > 2 and bfs(i) > 1:
            return "No"

    return "Yes"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []

    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        edges = []
        for _ in range(m):
            u = int(data[index])
            v = int(data[index + 1])
            edges.append((u, v))
            index += 2
        result = is_leaf_cactus(n, m, edges)
        results.append(result)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
