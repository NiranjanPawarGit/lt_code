# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        def helper(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            
            return helper(node.left, low, node.val) and helper(node.right, node.val, high)

        return helper(root, float('-inf'), float('inf'))

# Example to test the Solution class

# Creating a binary tree:
#       2
#      / \
#     1   3

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

# Instantiating the Solution class and checking if the tree is a valid BST
solution = Solution()
print(solution.isValidBST(root))  # Expected output: True

# Creating an invalid BST:
#       5
#      / \
#     1   4
#        / \
#       3   6

root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)

print(solution.isValidBST(root2))  # Expected output: False
