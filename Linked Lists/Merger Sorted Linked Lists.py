from LinkedList import ListNode

vals = [1, 2, 3, 4]
head = ListNode(vals[0])
tmp = head
for n in vals[1:]:
    tmp.next = ListNode(n)
    tmp = tmp.next

vals1 = [0, 1]
head1 = ListNode(vals1[0])
tmp = head1
for n in vals1[1:]:
    tmp.next = ListNode(n)
    tmp = tmp.next


def Merger(a: ListNode, b: ListNode):
    if a is None:
        return b
    elif b is None:
        return a

    if a.val < b.val:
        a.next = Merger(a.next, b)
        result = a
    else:
        b.next = Merger(a, b.next)
        result = b

    return result


r = Merger(head, head1)
print(r)
