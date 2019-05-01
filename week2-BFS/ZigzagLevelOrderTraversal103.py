from typing import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([(root,1)])
        res = []
        while queue:
            cur,level = queue.popleft()
            
            if len(res)<level:
                res.append([])
            res[level-1].append(cur.val)
            if level%2!=0:
                if cur.left:
                    queue.insert(0,(cur.left,level+1))
                if cur.right:
                    queue.insert(0,(cur.right,level+1))
            else:
                if cur.left:
                    queue.append((cur.left,level+1))
                if cur.right:
                    queue.append((cur.right,level+1))
        return res

sol = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(sol.zigzagLevelOrder(root))