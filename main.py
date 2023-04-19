from stacks import TestStackSolutions

STACK_PROBLEMS = ["20", "94"]

def execute():
    problem_num = input("Which problem number would you like test? ")
    print(f"\nOK, executing problem number {problem_num}.\n")

    if problem_num in STACK_PROBLEMS:
        test = TestStackSolutions()

        if problem_num == "20":
            test.testIsValid()
        elif problem_num == "94":
            test.testInorderTraversal()
        else:
            print("Sorry, this problem number hasn't been solved yet.\n")

    else:
        print("Sorry, this problem number hasn't been solved yet.\n")


if __name__ == "__main__":
    execute()
