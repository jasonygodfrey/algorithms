class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        #swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        #time complexity is O(n) since we visit each node once
        # space complexity  is O(n) since we have to store the recursive call stack
        """ Here is the explanation for the code above:
1. First, we check if the root is None. If it is None, we return None.
2. If the root is not None, we swap the children.
3. We call the function recursively for both children.
4. We return the root at the end. """