# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            return 1+max(height(root.left),height(root.right))
        if not root:
            return True
        return abs(height(root.left)-height(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    """ Here is the explanation for the code above:
1. We have a function height which takes the root of the tree as its argument.
2. Then we check if the root is null, if it is null, we return 0.
3. If it isn't, we return the height of the left subtree and the right subtree, whichever is greater.
4. Then we check if the root is null, if it is, we return True.
5. We return the absolute difference between the height of the left subtree and the right subtree, and we check if it is less than or equal to 1, and we also check if the left subtree is balanced and if the right subtree is balanced. """