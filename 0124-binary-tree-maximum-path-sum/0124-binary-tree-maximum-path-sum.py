# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxpathsum = -math.inf

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.maxpathsum

    def helper(self, node):
        if not node:
            return 0

        leftsum = max(0, self.helper(node.left))
        rightsum = max(0, self.helper(node.right))

        currentpathmax = node.val + leftsum + rightsum
        self.maxpathsum = max(self.maxpathsum, currentpathmax)

        return node.val + max(leftsum, rightsum)

        