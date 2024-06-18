class Solution:
    def minOperations(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = [root]
        operations = 0
        
        while queue:
            next_level = []
            for node in queue:
                if node.left and node.left.val > node.right.val:
                    node.left.val, node.right.val = node.right.val, node.left.val
                    operations += 1
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
        
        return operations