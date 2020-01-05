# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def hask(self, first: ListNode, k: int):
        while k > 0 and first:
            k = k - 1
            first = first.next

        return k == 0

    def reverseKGroup(self, first: ListNode, k: int) -> ListNode:

        if k == 1:
            return first

        if first is None or not self.hask(first, k):
            return first

        prev_node = None
        tail = first
        for i in range(0, k):
            # switch the links
            second = first.next

            first.next = prev_node

            # update the prev_node
            prev_node = first
            first = second

        tail.next = self.reverseKGroup(first, k)

        return prev_node


vals = [1, 2, 3, 4]

head = ListNode(vals[0])
tmp = head
for n in vals[1:]:
    tmp.next = ListNode(n)
    tmp = tmp.next

s = Solution()
head = s.reverseKGroup(head, 2)
print(head)
