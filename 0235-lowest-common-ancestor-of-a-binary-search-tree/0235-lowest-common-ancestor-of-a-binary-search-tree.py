# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
""" Here is the explanation for the code above:
1. We create a variable cur that will be used to traverse the tree
2. We start a while loop that will run until cur is not None, meaning we are not at the end of the tree
3. If both p and q are greater than the current node, we know we need to traverse to the right
4. If both p and q are less than the current node, we know we need to traverse to the left
5. If neither of the above conditions are met, we know we have found the LCA so we return it """