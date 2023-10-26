class Solution:
    def boundaryOfBinaryTree(self, root):
        if not root:
            return []

        def is_leaf(node):
            if not node:
                return False
            if not node.left and not node.right:
                return True

        def add_left_boundary(node, res):
            while node:
                if not is_leaf(node):
                    res.append(node.val)
                if node.left:
                    node = node.left
                else:
                    node = node.right

        def add_leaves(node, res):
            if node:
                if is_leaf(node):
                    res.append(node.val)
                else:
                    add_leaves(node.left, res)
                    add_leaves(node.right, res)

        def add_right_boundary(node, res):
            stack = []
            while node:
                if not is_leaf(node):
                    stack.append(node.val)
                if node.right:
                    node = node.right
                else:
                    node = node.left
            res += stack[::-1]

        boundary = []

		
        if not is_leaf(root):
            boundary.append(root.val)

        add_left_boundary(root.left, boundary)
        add_leaves(root, boundary)
        add_right_boundary(root.right, boundary)

        return boundary