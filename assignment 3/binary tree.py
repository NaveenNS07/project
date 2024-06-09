class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidSequence(root, arr):
    def check_path(node, index):
        if not node or node.val != arr[index]:
            return False
        if index == len(arr) - 1:
            return not node.left and not node.right
        return check_path(node.left, index + 1) or check_path(node.right, index + 1)

    return check_path(root, 0)

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right.left = None
root.right.right = None
root.left.left.left = None
root.left.left.right = None
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(0)

arr = [0, 1, 0, 1]
print(isValidSequence(root, arr))