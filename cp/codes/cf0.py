import sys

def update(tree, node, start, end, idx, val):
    if start == end:
        tree[node] = val
    else:
        mid = (start + end) // 2
        if start <= idx <= mid:
            update(tree, node * 2, start, mid, idx, val)
        else:
            update(tree, node * 2 + 1, mid + 1, end, idx, val)
        tree[node] = min(tree[node * 2], tree[node * 2 + 1])

def query(tree, node, start, end, left, right):
    if right < start or end < left:
        return sys.maxsize
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return min(query(tree, node * 2, start, mid, left, right), query(tree, node * 2 + 1, mid + 1, end, left, right))

def find_unsorted_subarray(arr):
    n = len(arr)
    tree = [0] * (4 * n)
    for i in range(n):
        update(tree, 1, 0, n - 1, i, arr[i])
    left, right = 0, n - 1
    while left < right:
        if arr[left] <= arr[left + 1]:
            left += 1
        else:
            break
    while right > left:
        if arr[right] >= arr[right - 1]:
            right -= 1
        else:
            break
    if left == right:
        return -1, -1
    min_val = query(tree, 1, 0, n - 1, left, right)
    max_val = query(tree, 1, 0, n - 1, left, right)
    while left > 0 and arr[left - 1] > min_val:
        left -= 1
    while right < n - 1 and arr[right + 1] < max_val:
        right += 1
    return left, right

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    q = int(input())
    print(*find_unsorted_subarray(arr))
    for _ in range(q):
        pos, val = map(int, input().split())
        arr[pos - 1] = val
        print(*find_unsorted_subarray(arr))