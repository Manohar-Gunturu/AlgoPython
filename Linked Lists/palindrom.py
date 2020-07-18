# Definition for singly-linked list.
import json


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 1, 2, 1
# 1, 2, 2, 1
class Solution:
    head: ListNode = None

    # 1 - > 2 -> 1
    def isPalindrome(self, h: ListNode) -> bool:
        self.head = h
        return self.isPal(h)

    def isPal(self, h):
        if h is None:
            return True

        if not self.isPal(h.next) or self.head.val != h.val:
            return False

        self.head = self.head.next

        return True




def stringToIntegerList(input):
    return json.loads(input)


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

    line = "[2, 1, 2]"
    head = stringToListNode(line);

    ret = Solution().isPalindrome(head)

    out = (ret);
    print(out)


if __name__ == '__main__':
    main()
