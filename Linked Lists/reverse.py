import json


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def stringToIntegerList(input):
    return json.loads(input)


class Solution:

    def printL(self, head):
        tmp: str = ""
        while head:
            tmp += "->" + str(head.val)
            head = head.next
        print(tmp)

    def reverse(self, head: ListNode):

        pointer = head
        # None <- 1 -> 2 - > 3
        prev = None
        while pointer:
            tmp = pointer.next
            pointer.next = prev
            prev = pointer
            pointer = tmp
        self.printL(prev)


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def main():
    import sys
    import io

    line = "[1, 2, 6, 2, 1]"
    head = stringToListNode(line);

    ret = Solution().reverse(head)

    out = (ret);
    print(out)
