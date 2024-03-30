from quacktools.utilities.utility import Utility

from quacktools.constants.argument_constants import URL_PREFIX


class App:
    def __init__(self):
        self.arguments = Utility.get_arguments()
        self.problem_number = self.get_problem_number()
        self.difficulty = self.arguments.difficulty
        self.compiler = None
        self.url = None

    def run(self):
        print(self.arguments)
        self.url = self.get_url()
        print(self.url)
        self.compiler = self.get_compiler()

    def get_problem_number(self):
        if self.arguments.problem is not None:
            return self.arguments.problem

        return self.arguments.contest

    def get_url(self):
        url = URL_PREFIX + ("/contest" if self.arguments.contest is not None else "/problem")

        return url + f"/{self.get_problem_number()}/{self.arguments.difficulty}"

    def get_compiler(self):
        pass
