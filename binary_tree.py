import collections
from typing import List, Optional
from unittest import TestCase
from utils import TreeNode, create_tree_from_list


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        103. Binary Tree Zigzag Level Order Traversal
        https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
        """
        zigzag_tree_values = []

        if not root or root.val is None:
            return zigzag_tree_values

        # Instantiate a levels counter to track our current depth in the tree
        curr_level = 0

        # Instantiate a queue (beginning with the root) to track which nodes we must visit next
        # (Why queue & not list? -> queue.popleft()'s time complexity O(1) while list.pop(0)'s time complexity is O(n))
        queue = collections.deque([root])
        while queue:
            curr_level_vals = []

            # Visit all the nodes in the current level
            for _ in range(len(queue)):
                # Get the first node in the queue
                node = queue.popleft()

                # Add the value of the current node to the list of values at the current level
                curr_level_vals.append(node.val)

                # Add the left and right children of the current node to the queue
                # so that we can track which nodes we need to visit in the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Use the levels counter to decide whether we need to zig or zag:
            # If the level is even, we can add the node values from left to right (zig).
            # If the level is odd, we can add the node values from right to left (zag).
            if curr_level % 2 != 0:
                curr_level_vals.reverse()

            zigzag_tree_values.append(curr_level_vals)

            curr_level += 1

        return zigzag_tree_values

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        112. Path Sum
        https://leetcode.com/problems/path-sum/
        """
        if root is None:
            return False

        stack = [(root, root.val)]

        while stack:
            curr_node, curr_sum = stack.pop()

            # The current node must be a leaf node to return true
            if curr_sum == targetSum and not curr_node.left and not curr_node.right:
                return True
            # If the current node is a leaf, but the sum is not what we desire, subtract its val to back track
            if curr_sum < targetSum and not curr_node.left and not curr_node.right:
                curr_sum -= curr_node.val

            if curr_node.left:
                stack.append((curr_node.left, curr_sum + curr_node.left.val))
            if curr_node.right:
                stack.append((curr_node.right, curr_sum + curr_node.right.val))

        return False

class TestBinaryTreeSolutions(TestCase):
    def testZigzagLevelOrder(self):
        test_data = [
            # Standard tests
            {
                "input": create_tree_from_list([3, 9, 20, None, None, 15, 7]),
                "output": [[3], [20, 9], [15, 7]]
            },
            {
                "input": create_tree_from_list([1]),
                "output": [[1]]
            },
            {
                "input": create_tree_from_list([]),
                "output": []
            },
            # Edge cases
        ]

        solution = Solution()
        for test in test_data:
            if test['input']:
                print(f"""Testing input {test['input'].val}.""")
            else:
                print(f"""Testing input {test['input']}.""")
            response = solution.zigzagLevelOrder(test["input"])
            try:
                self.assertEqual(response, test["output"])
            except:
                print(f"Solution failed! {response} != {test['output']} \n")

    def testHasPathSum(self):
        test_data = [
            # Standard tests
            {
                "input": [create_tree_from_list([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22],
                "output": True
            },
            {
                "input": [create_tree_from_list([1, 2, 3]), 5],
                "output": False
            },
            {
                "input": [create_tree_from_list([]), 0],
                "output": False
            },
            # Edge cases
        ]

        solution = Solution()
        for test in test_data:
            if test['input'][0]:
                print(f"""Testing input {test['input'][0].val}.""")
            else:
                print(f"""Testing input {test['input'][0]}.""")
            response = solution.hasPathSum(test["input"][0], test["input"][1])
            try:
                self.assertEqual(response, test["output"])
            except:
                print(f"Solution failed! {response} != {test['output']} \n")
