# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
       
        if root == None:
            return None
        
        queue = deque([root])

        while queue:
            curr = queue.popleft()
            if curr.val == val:
                return curr
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        return None


        #recursive
        
        # if root == None:
        #     return None
        
        # if root.val == val:
        #     return root

        # return self.searchBST(root.left, val) if val < root.val \
        #     else self.searchBST(root.right, val)