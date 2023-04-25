from typing import List
from unittest import TestCase


class Solution:

    def trappingRainWater(self, height: List[int]) -> int:
        """
        42. Trapping Rain Water
        https://leetcode.com/problems/trapping-rain-water/
        """
        h20 = 0
        listLen = len(height)

        # To trap water, we need at least 3 elements in the list (2 walls)
        if listLen < 3:
            return h20

        # Use pointers to move across list:
        l = 0
        r = listLen - 1

        # Initialize vars to remember our max bounds for wall height:
        leftMax = height[l]
        rightMax = height[r]

        # Traverse list:
        while l < r:
            # Compare our current maxHeights to see which height we are limited by, e.g. if we have 2 & 3, we are limited by the lower value 2.
            # The diff between maxHeight & the pointer's curr value is the amount of water trappable,
            # e.g. 2 units h20 for 3-1 in [3, 1, 2, 4] & 2 units h20 for 4-2 in [3, 1, 2, 4].
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                h20 += leftMax - height[l]
            # if rightMax < leftMax:
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                h20 += rightMax - height[r]

        return h20


class TestTwoPointerSolutions(TestCase):

    def testTrappingRainWater(self):
        test_data = [
            # Standard tests
            {
                "input": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
                "output": 6
            },
            {
                "input": [4, 2, 0, 3, 2, 5],
                "output": 9
            },
            # Edge cases
            {
                "input": [1, 2],
                "output": 0
            },
            {
                "input": [1, 1, 2],
                "output": 0
            },
            {
                "input": [1, 2, 3, 4, 3, 2, 1],
                "output": 0
            }
        ]

        solution = Solution()
        for test in test_data:
            print(f"""Testing input {test['input']}.""")
            response = solution.trappingRainWater(test["input"])
            try:
                self.assertEqual(response, test["output"])
            except:
                print(f"Solution failed! {response} != {test['output']} \n")
