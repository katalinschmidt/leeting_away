from unittest import TestCase

class Solution:
    def isValid(self, s: str) -> bool:
        """
            20. Valid Parentheses
            https://leetcode.com/problems/valid-parentheses/
        """
        # Things I know:
        # I must validate my str 1) contains chars and 2) each char is a valid parantheses
        # To be (potentially) balanced, the str length must be an even number
        # Rule of thumb - Balancing / reversing / validity requires a stack (list in Python), LIFO
        # I can add opening brackets to the stack, then pop off the stack once I encounter a closing bracket to see if they are the same type. E.g. "({})" -> Pop "{" once I see "}" & compare.
        # I will need to define my opening & closing bracket types for the computer

        # Confirm the str length is even
        if len(s) % 2 != 0:
            return False

        # Create the stack
        stack = []

        # Examine each char in the str
        for c in s:
            # If the char is an opening bracket, add it to the stack
            if c in ["(", "{", "["]:
                stack.append(c)
            # If the char is a closing bracket, compare it to the last opening bracket seen / last el added to the stack (LIFO)
            else:
                # Make sure we've already seen an opening bracket, otherwise we're looking at a case of closing brackets first / only
                if len(stack) == 0:
                    return False

                # If the brackets are not a match, return because we know our str is not balanced
                last_open = stack.pop()
                if last_open == "(" and c != ")":
                    return False
                if last_open == "{" and c != "}":
                    return False
                if last_open == "[" and c != "]":
                    return False

                # Otherwise, continue examining the str

        # Make sure we've exhausted the stack, otherwise we're looking at a case of only open brackets
        if len(stack) != 0:
            return False

        return True

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

