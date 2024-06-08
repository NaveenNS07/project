class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

def smallestStringWithSwaps(s, pairs):
    n = len(s)
    uf = UnionFind(n)
    for a, b in pairs:
        uf.union(a, b)
    
    from collections import defaultdict
    components = defaultdict(list)
    for i in range(n):
        root = uf.find(i)
        components[root].append(i)
    
    res = list(s)
    for comp in components.values():
        indices = sorted(comp)
        chars = sorted(res[i] for i in indices)

        for i, char in zip(indices, chars):
            res[i] = char
    
    return ''.join(res)

s = "dcab"
pairs = [[0, 3], [1, 2]]
print(smallestStringWithSwaps(s, pairs)) 
