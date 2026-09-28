class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.diameter = 0
        def solve(root):
            if root == None:
                return 0
            leftHeight = solve(root.left)
            rightHeight = solve(root.right)
            self.diameter = max(self.diameter,leftHeight + rightHeight)
            return 1 + max(leftHeight,rightHeight)
        solve(root)
        return self.diameter