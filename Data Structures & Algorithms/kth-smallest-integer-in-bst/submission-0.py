class Solution: # brutal
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        vals = []

        def dfs(node):
            if not node:
                return
            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        vals.sort()
        return vals[k - 1]