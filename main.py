from stacks import TestStackSolutions

def execute():
    problem_num = input("Which problem number would you like test? ")
    print(f"\nOK, executing problem number {problem_num}.\n")

    if problem_num in ["20"]:
        test = TestStackSolutions()

        if problem_num == "20":
            test.testIsValid()


if __name__ == "__main__":
    execute()
