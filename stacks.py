from typing import Optional, List
from unittest import TestCase
from utils import TreeNode


class Solution:
    def isValid(self, s: str) -> bool:
        """
        20. Valid Parentheses
        https://leetcode.com/problems/valid-parentheses/
        """
        # Odd str length immediately signals unbalanced parantheses
        if len(s) % 2 != 0:
            return False

        # Create the stack
        stack = []

        # Define valid brackets
        opening_brackets = ["(", "{", "["]
        bracket_pairings = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        # Examine each char in the str
        for c in s:
            # If the char is an opening bracket, add it's closing equivalent to the stack
            if c in opening_brackets:
                stack.append(bracket_pairings[c])
            # If the char is a closing bracket, compare it to the last opening bracket seen / last el added to the stack (LIFO)
            # Req: Make sure we've already seen an opening bracket, otherwise we're looking at a case of closing brackets first / only
            elif stack and stack[-1] == c:
                # If they match, remove the bracket from the stack, so we can successfully continue examining the rest of the string
                stack.pop()
            else:
                return False

        # Make sure we've exhausted the stack, otherwise we're looking at a case of only open brackets
        return len(stack) == 0

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        94. Binary Tree Inorder Traversal
        https://leetcode.com/problems/binary-tree-inorder-traversal/
        """
        # Create the stack & our results list
        stack = []
        result = []

        # Begin at the provided root
        current_node = root

        # Traverse until we've exhausted all nodes
        while current_node or stack:
            # Left traversal:
            while current_node:
                # Keep track of where we've been
                stack.append(current_node)
                # Traverse to left child
                current_node = current_node.left

            # Right traversal:
            # Once we've exhausted left children, return to root (last el in stack)
            current_node = stack.pop()
            # Save the value for our results list
            if current_node.val is not None:
                result.append(current_node.val)
            # Traverse to right child
            current_node = current_node.right

        return result


class TestStackSolutions(TestCase):
    def testIsValid(self):
        test_data = [
            # Standard tests
            {
                "input": "()",
                "output": True
            },
            {
                "input": "()[]{}",
                "output": True
            },
            {
                "input": "(]",
                "output": False
            },
            # Edge cases
            {
                "input": "(()))",
                "output": False
            },
            {
                "input": "((",
                "output": False
            },
            {
                "input": "){",
                "output": False
            },
        ]

        solution = Solution()
        for test in test_data:
            print(f"""Testing input "{test['input']}".""")
            response = solution.isValid(test["input"])
            try:
                self.assertEqual(response, test["output"])
            except:
                print(f"Solution failed! {response} != {test['output']} \n")

    def testInorderTraversal(self):
        # [1, None, 2, 3]
        tree1 = TreeNode(1)
        tree1.right = TreeNode(2)
        tree1.right.left = TreeNode(3)

        # []
        tree2 = TreeNode(None)

        # [1]
        tree3 = TreeNode(1)

        # [1, 2, None, 3, None]
        tree4 = TreeNode(1)
        tree4.left = TreeNode(2)
        tree4.right = None
        tree4.left.left = TreeNode(3)
        tree4.left.right = None

        test_data = [
            # Standard tests
            {
                "input": tree1,
                "output": [1, 3, 2]
            },
            {
                "input": tree2,
                "output": []
            },
            {
                "input": tree3,
                "output": [1]
            },
            # Edge cases
            {
                "input": tree4,
                "output": [3, 2, 1]
            },
        ]

        solution = Solution()
        for test in test_data:
            print(f"Testing input tree root {test['input'].val}.")
            response = solution.inorderTraversal(test["input"])
            try:
                self.assertEqual(response, test["output"])
            except:
                print(f"Solution failed! {response} != {test['output']} \n")
