from abc import ABC, abstractmethod


class Compiler(ABC):
    def __init__(self):
        self.file = ""
        self.extension = ""
        self.filename = ""
        self.filepath = ""
        self.user_outputs = None
        self.samples = None
        self.test_cases_passed = 0

    @abstractmethod
    def compile(self):
        pass

    @abstractmethod
    def get_program_output(self):
        pass

    def set_file(self, file):
        self.file = file
        self.filename, self.extension = file.split(".")

    def set_samples(self, samples):
        self.samples = samples
