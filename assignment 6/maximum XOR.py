from collections import defaultdict
from typing import List

class Solution:
    def maxSubTreeXOR(self, n: int, edges: List[List[int]], values: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        subtree_values = [0] * n
        def dfs(node, parent):
            subtree_values[node] = values[node]
            for neighbor in graph[node]:
                if neighbor != parent:
                    subtree_values[node] ^= dfs(neighbor, node)
            return subtree_values[node]
        
        def find_max_xor():
            max_xor = 0
            for i in range(n):
                for j in range(i + 1, n):
                    max_xor = max(max_xor, subtree_values[i] ^ subtree_values[j])
            return max_xor
        
        dfs(0, -1)
        return find_max_xor()
