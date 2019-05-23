from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return lists
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge(l, r)

    def merge(self, l, r):
        dummy = cur = ListNode(0) 
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return dummy.next

    def printNode(self, listnode):
        vals = ""''""
        while listnode:
            vals += str(listnode.val) + "--"
            listnode = listnode.next
        print(vals)

list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)
list2 = ListNode(2)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
lists = [list1, list2]
g = Solution()
ans = g.mergeKLists(lists) 
g.printNode(ans)
