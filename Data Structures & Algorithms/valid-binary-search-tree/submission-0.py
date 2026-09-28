# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        self.flag=True

        low=float("-inf")
        high=float("inf")

        def solve(root,low,high):

            if root is None:
                return

            if root.val<=low:
                self.flag=False
                return

            if root.val>=high:
                self.flag=False
                return

            if root.left and root.left.val>=root.val:
                self.flag=False
                return

            if root.right and root.right.val<=root.val:
                self.flag=False
                return

            left=solve(root.left,low,root.val)
            right=solve(root.right,root.val,high)

            return self.flag

        solve(root,low,high)

        return self.flag

        