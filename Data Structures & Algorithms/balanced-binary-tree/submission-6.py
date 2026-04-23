# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkbalance(node):
            if not node:
                return 0
            left_length = checkbalance(node.left)
            if left_length == -1:
                return -1

            right_length = checkbalance(node.right)
            if right_length == -1:
                return -1

            if abs (left_length - right_length) > 1:
                return -1
            
            return 1 + max(left_length, right_length)
        
        return checkbalance(root) != -1