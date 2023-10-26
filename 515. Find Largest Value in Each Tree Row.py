# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []
            
        queue = deque([root])
        arr = []
        while queue:
            curr_length = len(queue)
            curr_max = float('-inf')

            for _ in range(curr_length):
                curr = queue.popleft()
                curr_max = max(curr_max, curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            arr.append(curr_max)
        return arr


