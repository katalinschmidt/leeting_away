from typing import List
from unittest import TestCase


class Solution:
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

class TestSlidingWindowSolutions(TestCase):
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
