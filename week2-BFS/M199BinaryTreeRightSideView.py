from typing import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        res = []
        queue = deque([(root,0)])
        last_level = -1
        while queue:
            cur,level = queue.popleft() 
            if cur.right:
                queue.append((cur.right,level+1))
            if cur.left:
                queue.append((cur.left,level+1))
            if level > last_level:
                res.append(cur.val)
                last_level += 1
        return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

sol = Solution()

print(sol.rightSideView(root))

