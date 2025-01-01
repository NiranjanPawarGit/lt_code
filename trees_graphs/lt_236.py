class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        else:
            return l or r

# Example to test the Solution class

# Creating a binary tree:
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#        / \
#       7   4

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

p = root.left  # Node with value 5
q = root.left.right.right  # Node with value 4

solution = Solution()

lca = solution.lowestCommonAncestor(root, p, q)

# Output the result (the value of the LCA node)
print(f"The Lowest Common Ancestor of {p.val} and {q.val} is {lca.val if lca else None}")
