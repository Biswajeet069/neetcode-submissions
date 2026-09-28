# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        self.flag = False

        def solve(root, subroot):

            if subroot is None:
                return True

            if root is None:
                return False

            if root.val != subroot.val:
                left = solve(root.left, subroot)
                right = solve(root.right, subroot)
                return left or right

            if issame(root, subroot):
                return True

            return solve(root.left, subroot) or solve(root.right, subroot)

        def issame(root, subroot):

            if root is None and subroot is None:
                return True

            if root is None or subroot is None:
                return False

            if root.val != subroot.val:
                return False

            left = issame(root.left, subroot.left)
            right = issame(root.right, subroot.right)

            return left and right

        return solve(root, subRoot)

             
            
        