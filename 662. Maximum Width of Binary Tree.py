# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root==None:
            return 0
        
        maxWidth = 0
        queue = deque()
        queue.append((root, 0))

        while queue:
            curr_length = len(queue)
            _, level_head_index = queue[0]
              

            for _ in range(curr_length):
                curr, col_index = queue.popleft()
                # arr[level].append(curr.val)

                if curr.left:
                    queue.append((curr.left, 2* col_index))
                if curr.right:
                    queue.append((curr.right, 2* col_index+1))
            maxWidth = max(maxWidth, col_index-level_head_index+1)
                
            

        
        return maxWidth