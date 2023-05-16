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

    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        643. Maximum Average Subarray I
        https://leetcode.com/problems/maximum-average-subarray-i/
        """
        # Initialize window to first subarray of size k
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Iterate over remaining elements in array
        for i in range(k, len(nums)):
            # Increment window by adding current el of the new window & removing first el of the prev window
            window_sum += nums[i] - nums[i - k]
            # Update max sum with the greater of the two
            max_sum = max(max_sum, window_sum)

        # Return avg
        return max_sum / k


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

    def testFindMaxAverage(self):
        test_data = [
            # Standard tests
            {
                "input": [[1, 12, -5, -6, 50, 3], 4],
                "output": 12.75000
            },
            {
                "input": [[5], 1],
                "output": 5.00000
            },
            # Edge cases
            {
                "input": [[-1, -2, -3, -4], 2],
                "output": -1.50000
            },
            {
                "input": [[1, 2, 3, 4], 3],
                "output": 3.00000
            },
            {
                "input": [[1, -2, 3, -4], 2],
                "output": 0.50000
            },
            {
                "input": [[4, 0, 3, 1], 2],
                "output": 2.00000
            }
        ]

        solution = Solution()
        for test in test_data:
            print(f"""Testing input {test['input'][0]}.""")
            response = solution.findMaxAverage(test["input"][0], test["input"][1])
            try:
                self.assertEqual(response, test["output"])
            except:
                print(f"Solution failed! {response} != {test['output']} \n")
