# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        s = set()
        output = False
        def traverse(node):
            if node == None:
                return False
            
            elif k-node.val in s:
                return True
            else:
                s.add(node.val)
                return traverse(node.left) or traverse(node.right)

        return traverse(root)

    

        
