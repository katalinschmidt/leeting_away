from typing import List, Optional
from unittest import TestCase
from utils import TreeNode


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        103. Binary Tree Zigzag Level Order Traversal
        https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
        """
        pass


class TestBinaryTreeSolutions(TestCase):
    def testZigzagLevelOrder(self):
        test_data = [
            # Standard tests
            {
                "input": [3, 9, 20, None, None, 15, 7],
                "output": [[3], [20, 9], [15, 7]]
            },
            {
                "input": [1],
                "output": [[1]]
            },
            {
                "input": [],
                "output": []
            },
            # Edge cases

        ]

        solution = Solution()
        for test in test_data:
            print(f"""Testing input {test['input']}.""")
            response = solution.zigzagLevelOrder(test["input"], test["input"])
            try:
                self.assertEqual(response, test["output"])
            except:
                print(f"Solution failed! {response} != {test['output']} \n")
