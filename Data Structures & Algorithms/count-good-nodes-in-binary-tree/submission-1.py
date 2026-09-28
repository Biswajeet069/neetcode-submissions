# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def solve(root, high):

            if root is None:
                return 0

            count = 0

            if root.val >= high:
                count += 1
                high = root.val

            left = solve(root.left, high)
            right = solve(root.right, high)

            return  count+left + right

        return solve(root, root.val)
        
            
            
        

            
        