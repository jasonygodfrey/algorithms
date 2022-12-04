# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        mid =  inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root
        
        """ Here is the explanation for the code above:
1. First, we need to understand the preorder and inorder traversal. Preorder traversal is going from the root to the left subtree and then to the right subtree. Inorder traversal is going from the left subtree to the root and then to the right subtree. In the first line of code, we check if the preorder and inorder arrays are empty. If they are empty, we return None. If they are not empty, we create a root node from the first element of the preorder array.
2. Next, we need to find the root node in the inorder array. We use the index() method to find the index of the root node in the inorder array. The index() method returns the first index of the value that we are looking for. For example, if we are looking for the value 5 in the array [3, 5, 2, 5], the index() method will return 1, because 5 is the first element that we are looking for.
3. Next, we use the index of the root node to divide the inorder array into two parts. The first part is the left subtree, and the second part is the right subtree. The index of the root node is the number of elements in the left subtree.
4. We use the left subtree to divide the preorder array into two parts. The first part is the left subtree, and the second part is the right subtree.
5. We use the left subtree of the preorder array to create the left subtree of the root node. We use the left subtree of the inorder array to create the left subtree of the root node.
6. We use the right subtree of the preorder array to create the right subtree of the root node. We use the right subtree of the inorder array to create the right subtree of the root node.
7. Finally, we return the root node. """
""" The code above does the following, explained in English:
1. If the preorder or inorder lists are empty, return None
2. Create a node with preorder[0] as the root
3. Find the root in the inorder list
4. Make the left subtree by recursively calling buildTree() on the left side of the root in the preorder and inorder lists
5. Make the right subtree by recursively calling buildTree() on the right side of the root in the preorder and inorder lists
6. Return the root node """
        
        