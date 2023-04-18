from unittest import TestCase

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
            try:
                self.assertEqual(solution.isValid(test["input"]), test["output"])
            except:
                print("Solution failed!\n")

