class TreeNode:
    def _init_(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closestNodesQueries(root, queries):
    def findClosest(node, target, closest):
        if not node:
            return closest
        if node.val <= target:
            closest[0] = max(closest[0], node.val)
            findClosest(node.right, target, closest)
        else:
            closest[1] = min(closest[1], node.val)
            findClosest(node.left, target, closest)
    
    def findClosestNodes(node, query):
        closest = [-1, -1]
        findClosest(node, query, closest)
        return closest
    
    def createAnswer(root, queries):
        answer = []
        for query in queries:
            answer.append(findClosestNodes(root, query))
        return answer
    
    return createAnswer(root, queries)

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(13)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right.left = TreeNode(9)
root.right.right = TreeNode(15)
root.right.right.left = TreeNode(14)

queries = [2, 5, 16]
output = closestNodesQueries(root, queries)
print(output) 