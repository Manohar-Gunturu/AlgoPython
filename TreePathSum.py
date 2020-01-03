data = [
    [0, 1, 8],
    [0, 2, 9],
    [1, 3, 5],
    [1, 4, 6],
    [2, 5, 0]
]


class Node:
    def __init__(self, left, right, val):
        self.left = left
        self.right = right
        self.val = val


class Solution:
    def hasPathSum(self, root: Node, sum: int) -> bool:

        stack = []
        stack.append((root, sum))
        while len(stack) > 0:

            cnode, cval = stack.pop()
            if cnode is None:
                break

            val = cnode.val
            if cnode.left is not None:
                stack.append((cnode.left, cval - val))
            if cnode.right is not None:
                stack.append((cnode.right, cval - val))
            if cnode.left is None and cnode.right is None:
                if val - cval == 0:
                    return True

        return False


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = Node(int(inputValues[0]))
    nodeQueue = [root]
    index = 1
    while index < len(inputValues):
        node = nodeQueue.po(0)

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = Node(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = Node(rightNumber)
            nodeQueue.append(node.right)
    return root
