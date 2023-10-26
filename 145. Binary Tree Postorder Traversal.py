# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        arr = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            
            if node.right:
                traverse(node.right)
            arr.append(node.val)
        
        if root==None:
            return arr
        traverse(root)
        return arr