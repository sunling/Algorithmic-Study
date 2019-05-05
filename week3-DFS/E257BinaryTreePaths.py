from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#Given a binary tree, return all root-to-leaf paths.
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        stack= [(root,'')]
        res = []
        while stack:
            #print('------------------')
            #print('stack:',[(i[0].val,i[1]) for i in stack])
            node, path = stack.pop()
            if node.right:
                stack.append((node.right, path + str(node.val)+'->'))
            if node.left:
                stack.append((node.left, path + str(node.val)+'->'))
            if not node.left and not node.right:
                res.append(path + str(node.val))
        return res 
    
    def binaryTreePathsRecursive(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        self.dfs(root,'',res)
        return res

    def dfs(self,node:TreeNode,path,res):
        if not node.left and not node.right:
            path = path + str(node.val)
            res.append(path)
            return
        if node.left:
            self.dfs(node.left,path+str(node.val)+'->',res)
        if node.right:
            self.dfs(node.right,path+str(node.val)+'->',res)
        
 
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
sol = Solution()
print(sol.binaryTreePaths(root))

print(sol.binaryTreePathsRecursive(root))


        