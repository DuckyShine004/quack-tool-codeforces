from quacktools.compiler.cpp_compiler import CPPCompiler
from quacktools.utilities.utility import Utility

from quacktools.constants.argument_constants import URL_PREFIX


class App:
    def __init__(self):
        self.arguments = Utility.get_arguments()
        self.compiler = self.get_compiler()
        self.url = self.get_url()

    def run(self):
        self.compiler.initialize()
        self.compiler.compile()
        self.compiler.get_program_output()
        self.compiler.test_samples_with_user_output()

    def get_problem_number(self):
        if self.arguments.problem is not None:
            return self.arguments.problem

        return self.arguments.contest

    def get_url(self):
        url = URL_PREFIX + ("/contest" if self.arguments.contest is not None else "/problem")
        return "https://codeforces.com/problemset/problem/1950/F"
        return url + f"/{self.get_problem_number()}/{self.arguments.difficulty}"

    def get_compiler(self):
        extension = self.arguments.file.split(".")[1]

        match extension:
            case "cpp":
                return CPPCompiler(self)

        return None
