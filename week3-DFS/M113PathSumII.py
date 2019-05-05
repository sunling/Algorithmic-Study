from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

##Given a binary tree and a sum, find all root-to-leaf paths
##where each path's sum equals the given sum.
class Solution:
    def pathSum(self, root: TreeNode, t: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        
        def dfs(node, path):
            if not node.left and not node.right:  
                if sum(path) == t: 
                    res.append(path) 
            if node.left: 
                dfs(node.left, path + [node.left.val])
            if node.right:
                dfs(node.right, path + [node.right.val])
                
        dfs(root, [root.val])
        return res
    
g = Solution()
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)

print(g.pathSum(root,22))




    
