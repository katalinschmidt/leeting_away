from typing import Optional, List
from unittest import TestCase
from utils import TreeNode, create_tree_from_list


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

    def longestValidParentheses(self, s: str) -> int:
        """
        32. Longest Valid Parentheses
        https://leetcode.com/problems/longest-valid-parentheses/
        """
        longest_substr = 0
        # Initialize stack with -1, so that it is guaranteed to be less than the index of the first opening parenthesis char
        stack = [-1]

        for char, i in enumerate(s):
            # If the given char is an opening parenthesis, track its index
            if char == "(":
                stack.append(i)
            # If the given char is a closing parentheses...
            else:
                # Pop the last index (typically, it's corresponding opening parenthesis)
                stack.pop()
                # If the stack is empty, it means that there are no unmatched opening parentheses in the stack
                # and the current closing parenthesis at idx i does not match with any previous opening parentheses.
                # In this case, we push the current idx to the stack to mark the end of the previous valid substr / the start of a new potential valid substr.
                if not stack:
                    stack.append(i)
                else:
                    # curr_substr == i - stack[-1]
                    longest_substr = max(longest_substr, i - stack[-1])

        return longest_substr

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        239. Sliding Window Maximum
        https://leetcode.com/problems/sliding-window-maximum/
        """
        maxVals = []
        stack = []

        n = len(nums)
        for i in range(n):
            # stack[-1] represents the largest val we've seen so far in the window
            # If our current val is greater than that^, we have a new max & can remove the prev max from the stack
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            # Track the current value's idx because it might be the current window's max or future windows' max
            stack.append(i)

            # Check whether the leftmost window element is still within bounds. If it isn't, remove its idx from the stack.
            leftmost_window_idx = stack[0]
            if i - leftmost_window_idx >= k:
                stack.pop(0)

            # Once we've reach the end of our window, save the greatest val in the window in maxVals
            if i >= k - 1:
                maxVals.append(nums[stack[0]])

        return maxVals


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
        test_data = [
            # Standard tests
            {
                "input": create_tree_from_list([1, None, 2, 3]),
                "output": [1, 3, 2]
            },
            {
                "input": create_tree_from_list([]),
                "output": []
            },
            {
                "input": create_tree_from_list([1]),
                "output": [1]
            },
            # Edge cases
            {
                "input": create_tree_from_list([1, 2, None, 3, None]),
                "output": [3, 2, 1]
            },
        ]

        solution = Solution()
        for test in test_data:
            if test['input']:
                print(f"""Testing input {test['input'].val}.""")
            else:
                print(f"""Testing input {test['input']}.""")
            response = solution.inorderTraversal(test["input"])
            try:
                self.assertEqual(response, test["output"])
            except:
                print(f"Solution failed! {response} != {test['output']} \n")

    def testLongestValidParentheses(self):
        test_data = [
            # Standard tests
            {
                "input": "(()",
                "output": 2
            },
            {
                "input": ")()())",
                "output": 4
            },
            {
                "input": "",
                "output": 0
            },
            # Edge cases
            {
                "input": "()(()",
                "output": 2
            },
        ]

        solution = Solution()
        for test in test_data:
            print(f"""Testing input "{test['input']}".""")
            response = solution.longestValidParentheses(test["input"])
            try:
                self.assertEqual(response, test["output"])
            except:
                print(f"Solution failed! {response} != {test['output']} \n")

    def testMaxSlidingWindow(self):
        test_data = [
            # Standard tests
            {
                "input": [[1, 3, -1, -3, 5, 3, 6, 7], 3],
                "output": [3, 3, 5, 5, 6, 7]
            },
            {
                "input": [[1], 1],
                "output": [1]
            },
            # Edge cases
            {
                "input": [[1, 2, 3, 4, 5], 3],
                "output": [3, 4, 5]
            },
            {
                "input": [[5, 4, 3, 2, 1], 3],
                "output": [5, 4, 3]
            },
            {
                "input": [[1, 2, 1, 1, 1, 1], 2],
                "output": [2, 2, 1, 1, 1]
            },
        ]

        solution = Solution()
        for test in test_data:
            print(f"""Testing input {test['input']}.""")
            response = solution.maxSlidingWindow(test["input"][0], test["input"][-1])
            try:
                self.assertEqual(response, test["output"])
            except:
                print(f"Solution failed! {response} != {test['output']} \n")
