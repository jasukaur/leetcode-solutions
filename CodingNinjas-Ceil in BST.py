from os import *
from sys import *
from collections import *
from math import *
from queue import deque

# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

#     Following is the TreeNode class structure

#     class TreeNode:

#         def __init__ (self, data):

#             self.data = data
#             self.left = None
#             self.right = None
            
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


def floorInBST(root, x, floor=-1):
    if root == None:

        return floor

    if root.data==x:

        return root.data

    if root.data<x:

        floor=root.data

        return floorInBST(root.right, x, floor)

    else:

        return floorInBST(root.left, x, floor)