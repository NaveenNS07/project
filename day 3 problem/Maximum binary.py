class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructMaximumBinaryTree(nums):
    if not nums:
        return None
    
    max_val = max(nums)
    max_index = nums.index(max_val)
    
    root = TreeNode(max_val)
    root.left = constructMaximumBinaryTree(nums[:max_index])
    root.right = constructMaximumBinaryTree(nums[max_index + 1:])
    
    return root

nums = [3,2,1,6,0,5]
root = constructMaximumBinaryTree(nums)
