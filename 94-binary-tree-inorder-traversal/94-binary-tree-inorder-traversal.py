# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res
        """ Here is the explanation for the code above:
1. First we create a function inorder() which will traverse the tree in inorder manner.
2. If the root is not None then we call the function recursively for the left subtree.
3. Then we add the root value to the list.
4. Then we call the function recursively for the right subtree.
5. Then we call the function inorder() and pass the root of the tree as a parameter.
6. Then we return the list. """