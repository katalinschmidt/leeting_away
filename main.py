from stacks import TestStackSolutions

# Map problem numbers to their respective test methods
STACK_PROBLEMS = {
    "20": "testIsValid",
    "94": "testInorderTraversal",
    "32": "testLongestValidParentheses",
    "42": "testTrappingRainWater"
}

def execute():
    problem_num = input("Which problem number would you like test? ")
    print(f"\nOK, executing problem number {problem_num}.\n")

    # Check if the problem number is valid
    if problem_num not in STACK_PROBLEMS:
        print("Sorry, this problem number hasn't been solved yet.\n")
        return

    # Call the corresponding test method
    test = TestStackSolutions()
    method_name = STACK_PROBLEMS[problem_num]
    try:
        getattr(test, method_name)()
    except Exception as e:
        print(f"An error occurred while running {method_name}: {str(e)}")

if __name__ == "__main__":
    execute()
