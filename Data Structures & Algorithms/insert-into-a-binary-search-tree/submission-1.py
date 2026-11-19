# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
            10
        7         15
    4      8
 3     6      
        """
        found = False
        if not root:
            return TreeNode(val)
        def dfs(node):
            nonlocal found
            if not node or found:
                return None
            
            if node.val > val:
                if not node.left:
                    print(node)
                    node.left = TreeNode(val)
                    found = True
                else:
                    dfs(node.left)
            else:
                if not node.right:
                    print(node)
                    node.right = TreeNode(val)
                    found = True
                else:
                    dfs(node.right)
        dfs(root)
        return root