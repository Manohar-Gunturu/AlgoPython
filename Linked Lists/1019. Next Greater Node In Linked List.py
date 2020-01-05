# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def nextLargerNodes(head: ListNode) -> List[int]:

    stack, res, node = [], [], head
    while node:
        while len(stack) and stack[-1][0] < node.val:
            res[stack.pop()[1]] = node.val
        stack.append((node.val, len(res)))
        res.append(0)
        node = node.next
    return res


vals = [2, 7, 3, 4, 5]

head = ListNode(vals[0])
tmp = head
for n in vals[1:]:
    tmp.next = ListNode(n)
    tmp = tmp.next

nextLargerNodes(head)