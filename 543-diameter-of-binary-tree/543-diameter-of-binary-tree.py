# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(root):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], left + right + 2)
            return max(left, right) + 1
        dfs(root)
        return res[0]

""" Here is the explanation for the code above:
1. define a variable res to store the maximum diameter we have found so far, and initialize it to 0
2. define a function dfs to recursively find the maximum diameter
3. in the function dfs, we first check if the root is None, if it is, then return -1
4. if the root is not None, then we recursively call dfs on the left and right child, and assign the result to left and right
5. we update the maximum diameter we have found so far by comparing the current res with the sum of left and right
6. we return the maximum of left and right plus 1
7. we call dfs on the root
8. we return the result stored in res """