# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        
        stack = []
        cur = root
        
        while cur or stack: #while cur is not null or stack is non empty
            while cur:
                stack.append(cur)

                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right
        
            """ The code above does the following, explained in English:
1. we have a stack and a variable n
2. we keep checking if the stack is non empty or the current node is not null
3. if the current node is not null, we add it to the stack and move to the left child
4. if the current node is null, we pop a node from the stack and add 1 to n
5. if n is equal to k, we return the value of the popped node
6. if n is not equal to k, we move to the right child of the popped node and repeat the process """
        