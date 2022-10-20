class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        
        return (self.isSameTree(p.left, q.left) and
        self.isSameTree(p.right, q.right))
        

        #time complexity O(n) 
        # space complexity O(n)

""" Here is the explanation for the code above:
1. Check if both p and q are None. If yes, return True.
2. Check if either p or q is None or p.val != q.val. If yes, return False.
3. Recursively call the function with p.left and q.left and p.right and q.right as arguments. """

""" Here is the explanation for the code above:
1. If the two trees are both None, they are the same
2. If one of the trees are None and the other one is not, they are not the same
3. If the values of the two trees are not the same, they are not the same
4. If the values of the two trees are the same, we need to check the children of the two trees 
   recursively to see if they are the same """