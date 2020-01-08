from LinkedList import ListNode

vals = [4, 2, 1, 3]
head = ListNode(vals[0])
tmp = head
for n in vals[1:]:
    tmp.next = ListNode(n)
    tmp = tmp.next

dummy_node = ListNode(-1)
dummy_node.next = head

prev_node = head

next_node: ListNode = head.next
current_pos = 0

while next_node:
    key = next_node.val
    node = dummy_node.next
    current_pos = current_pos + 1
    i = 0
    tmp_prev = dummy_node
    while i < current_pos and node.val <= key:
        i += 1
        tmp_prev = node
        node = node.next

    # next_node should be before node
    if current_pos != i:
        up_coming = next_node.next
        prev_node.next = next_node.next
        tmp_prev.next = next_node
        next_node.next = node

        next_node = up_coming

        continue

    prev_node = next_node
    next_node = next_node.next

print(dummy_node)
