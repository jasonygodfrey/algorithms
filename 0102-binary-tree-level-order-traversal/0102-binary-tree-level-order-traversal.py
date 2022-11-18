# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [] #result array
        q = collections.deque() #queue data structure
        q.append(root)
        
        while q: # while q is non empty
            qLen = len(q) #loop through que length 1 level at a  time
            level = [] #add to its own list then add list to res list
            for i in range(qLen): #loop through every value in this queue currently so qLen
                node = q.popleft() #pop nodes in from the left side of the quee first in first out
                if node: #if node is not null
                    level.append(node.val) #append the level to the lsit node
                    q.append(node.left) #add the children of these nodes
                    q.append(node.right)
            if level: #if level is non empty
                res.append(level) #you can append levels?!
        return res #return result
    