from abc import ABC, abstractmethod

from quacktools.utilities.logger import Logger
from quacktools.utilities.utility import Utility

from quacktools.constants.table_constants import TERMINAL_COLORS, TEST_CASE_OUTPUT_COLUMNS

from typing import List, Dict


class Compiler(ABC):
    def __init__(self, app):
        self.app = app
        self.file: str = ""
        self.filename: str = ""
        self.extension: str = ""
        self.user_outputs: List[str] = []
        self.samples: Dict[str, List[str]] = {}

    @abstractmethod
    def compile(self):
        pass

    @abstractmethod
    def get_program_output(self):
        pass

    def initialize(self):
        self.set_file()
        self.set_samples()

    def get_test_case_result(self, sample_output, user_output):
        if sample_output == user_output:
            return f"{TERMINAL_COLORS['green']}AC{TERMINAL_COLORS['default']}"

        return f"{TERMINAL_COLORS['red']}WA{TERMINAL_COLORS['default']}"

    def set_file(self):
        self.file = self.app.arguments.file
        self.filename, self.extension = self.app.arguments.file.split(".")

    def set_samples(self):
        self.samples = Utility.get_samples(self.app.url)

    def test_samples_with_user_output(self):
        test_cases = len(self.samples["input"])
        test_case_indices = []
        test_case_results = []
        sample_inputs = []
        sample_outputs = []

        for test_index in range(test_cases):
            test_case_indices.append(test_index + 1)
            sample_output = "".join(self.samples["output"][test_index])
            sample_inputs.append("".join(self.samples["input"][test_index]))
            sample_outputs.append(sample_output)
            test_case_results.append(self.get_test_case_result(sample_output, self.user_outputs[test_index]))

        rows = zip(test_case_indices, sample_inputs, sample_outputs, self.user_outputs, test_case_results)
        Logger.log_custom_table(TEST_CASE_OUTPUT_COLUMNS, rows)
