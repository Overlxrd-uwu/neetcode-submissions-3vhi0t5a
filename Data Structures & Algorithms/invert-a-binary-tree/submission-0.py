# Definition for a binary tree node.
# class TreeNode:
from os import RTLD_DEEPBIND
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # self.left = right self.right=left ; make sure you familiar with pointer and node
        if not root:
            return None
        
        tmp=root.left
        root.left=root.right
        root.right=tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

