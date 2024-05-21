# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.map = {}

    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.helper(root, True), self.helper(root, False))

    def helper(self, node, rob):
        if not node:
            return 0

        if (node, rob) in self.map:
            return self.map[(node, rob)]

        cash1 = 0
        if rob : 
            cash1 = node.val + self.helper(node.left, False) + self.helper(node.right, False)
        
        cash2 = self.helper(node.left, True) + self.helper(node.right, True)
        self.map[(node, rob)] = max(cash1, cash2)
        return self.map[(node, rob)]