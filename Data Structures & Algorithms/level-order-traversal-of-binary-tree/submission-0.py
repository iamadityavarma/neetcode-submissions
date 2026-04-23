# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        temp_list = []

        queue = collections.deque()

        queue.append(root)

        while queue:
            level = []
            qlen = len(queue)

            for i in range(qlen):
                current = queue.popleft()
                if current:
                    level.append(current.val)
                    queue.append(current.left)
                    queue.append(current.right)
            if level:
                temp_list.append(level)

        return temp_list



            



        
        

        