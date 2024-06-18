class TreeNode:
    def _init_(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def removeSubtree(root, target):
    if not root:
        return None
    if root.val == target:
        return None
    root.left = removeSubtree(root.left, target)
    root.right = removeSubtree(root.right, target)
    return root

def heightAfterSubtreeRemoval(root, queries):
    result = []
    for query in queries:
        root = removeSubtree(root, query)
        result.append(height(root))
    return result

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(4)
root.left.left = TreeNode(2)
root.right.right = TreeNode(6)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(7)
queries = [4]
print(heightAfterSubtreeRemoval(root, queries))  