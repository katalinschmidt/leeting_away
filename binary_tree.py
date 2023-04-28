import collections
from typing import List, Optional
from unittest import TestCase
from utils import TreeNode


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
        # while ensuring the zigzag pattern is maintained
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






class TestBinaryTreeSolutions(TestCase):
    def testZigzagLevelOrder(self):
        # [3, 9, 20, None, None, 15, 7]
        tree1 = TreeNode(3)
        tree1.left = TreeNode(9)
        tree1.right = TreeNode(20)
        tree1.right.left = TreeNode(15)
        tree1.right.right = TreeNode(7)

        # [1]
        tree2 = TreeNode(1)

        # []
        tree3 = TreeNode(None)

        test_data = [
            # Standard tests
            {
                "input": tree1,
                "output": [[3], [20, 9], [15, 7]]
            },
            {
                "input": tree2,
                "output": [[1]]
            },
            {
                "input": tree3,
                "output": []
            },
            # Edge cases
        ]

        solution = Solution()
        for test in test_data:
            print(f"""Testing input {test['input'].val}.""")
            response = solution.zigzagLevelOrder(test["input"])
            try:
                self.assertEqual(response, test["output"])
            except:
                print(f"Solution failed! {response} != {test['output']} \n")
