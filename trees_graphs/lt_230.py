from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        alist = inorder(root)
        return alist[k-1]

# Example to test the Solution class

# Creating a binary search tree (BST):
#         5
#        / \
#       3   6
#      / \
#     2   4
#    /
#   1

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

# Instantiate the Solution class
solution = Solution()

# Test case 1: Find the 3rd smallest element in the BST
k = 3
print(f"The {k}th smallest element is: {solution.kthSmallest(root, k)}")  # Expected output: 3

# Test case 2: Find the 1st smallest element in the BST
k = 1
print(f"The {k}th smallest element is: {solution.kthSmallest(root, k)}")  # Expected output: 1

# Test case 3: Find the 5th smallest element in the BST
k = 5
print(f"The {k}th smallest element is: {solution.kthSmallest(root, k)}")  # Expected output: 5
