from stacks import TestStackSolutions
from two_pointers import TestTwoPointerSolutions
from sliding_window import TestSlidingWindowSolutions

# Map problem numbers to their respective test methods
PROBLEM_TESTS = {
    # Stack
    "20": ("testIsValid", TestStackSolutions),
    "94": ("testInorderTraversal", TestStackSolutions),
    "32": ("testLongestValidParentheses", TestStackSolutions),
    # Two Pointer
    "42": ("testTrappingRainWater", TestTwoPointerSolutions),
    # Sliding Window
    "239": ("testMaxSlidingWindow", TestSlidingWindowSolutions),
}


def execute():
    problem_num = input("Which problem number would you like test? ")

    if problem_num not in PROBLEM_TESTS:
        print("Sorry, this problem number hasn't been solved yet.\n")
        return

    print(f"\nOK, executing problem number {problem_num}.\n")

    # Call the corresponding test method
    method_name, test_class = PROBLEM_TESTS[problem_num]
    test = test_class()
    try:
        getattr(test, method_name)()
    except Exception as e:
        print(f"An error occurred while running {method_name}: {str(e)}")


if __name__ == "__main__":
    execute()
