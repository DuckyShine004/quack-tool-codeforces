class Compiler:
    def __init__(self):
        self.test_cases_passed = 0

    def compile(self, extension):
        match extension:
            case "cpp":
                ...
            case _:
                print("Invalid filetype")

    def run_samples(self, samples):
        extension = ...
        self.compile(extension)

        # After compiling, we get the output of the user's answers through an output file
        # Next we compare the test case output with the user's outputs

    def compare_test_case_and_user_output(self, test_case_output):
        ...

        user_output = "lol"

        if user_output == test_case_output:
            self.test_cases_passed
