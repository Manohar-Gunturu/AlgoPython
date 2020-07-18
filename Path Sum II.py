# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, S: int) -> int:

        def dfs(node, sums, currSum):
            if not node:
                return

            newSum = node.val + currSum
            if newSum - S in sums:
                ans["num"] += sums[node.val + currSum - S]
            if not node.left and not node.right:
                return

            sums[newSum] = sums.get(newSum, 0) + 1
            dfs(node.left, sums, newSum)
            dfs(node.right, sums, newSum)
            sums[newSum] -= 1

        if not root:
            return 0

        ans = {"num": 0}
        sums = {0: 1}
        dfs(root, sums, 0)
        return ans["num"]


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
