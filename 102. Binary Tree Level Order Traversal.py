# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        arr = []
        level = 0
        queue = deque([root])

        if root==None:
            return arr

        while queue:
            curr_length = len(queue)
            arr.append([])  
            

            for i in range(curr_length):
                curr = queue.popleft()
                arr[level].append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            level +=1
        # print(arr)
        
        return arr
                


