# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        List = []
        if not root:
            return List
        queue = collections.deque()
        right = None
        queue.append(root)
        while queue:
            length = len(queue)

            for i in range(length):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            List.append(current.val)
        return List

            



           
        