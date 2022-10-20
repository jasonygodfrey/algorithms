# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        

        #time complexity O(n) 
        # space complexity O(n) 
""" Here is the explanation for the code above:
1. The base case: if the root is None, return 0, because the depth is 0.
2. Recursion: return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
   This is the recursion step. The recursion step is to find the maximum depth of the left subtree and the right subtree. And the maximum depth of the root is 1 + max(left subtree's depth, right subtree's depth). """