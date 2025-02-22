import collections

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

def dfs(al):
    stack = ['g']
    visited = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)    
            for x in al[node]:
                stack.append(x)
    print(visited)

def makelist(root):
    if root is None:
        return
    else:
        d[root.data] = []
        makelist(root.left)
        if root.left:
            d[root.data].append(root.left.data)
        if root.right:
            d[root.data].append(root.right.data)
        makelist(root.right)
    return d    

if __name__ == '__main__':
    root = Node('g')
    root.insert('c')
    root.insert('b')
    root.insert('a')
    root.insert('e')
    root.insert('d')
    root.insert('f')
    root.insert('i')
    root.insert('h')
    root.insert('j')
    root.insert('k')
    
    d = {}
    aList = makelist(root)
    dfs(aList)
    
