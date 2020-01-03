# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def pathSum(self, root: TreeNode, target: int) -> int:
        self.tracker = {0: 1}
        self.count = 0
        self.dfs(root, 0, target)
        return self.count

    def dfs(self, node, acc_sum, target):

        if node is None:
            return

        val = node.val

        acc_sum = acc_sum + val

        # print(acc_sum, target)

        if acc_sum - target in self.tracker:
            self.count += 1

        self.tracker[acc_sum] = 0

        self.dfs(node.left, acc_sum, target)
        self.dfs(node.right, acc_sum, target)

        if acc_sum in self.tracker:
            del self.tracker[acc_sum]


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


s = "[1,-2,-3,1,3,-2,null,-1]"
sol = Solution()
r = sol.pathSum(stringToTreeNode(s), 3)
print(r)
