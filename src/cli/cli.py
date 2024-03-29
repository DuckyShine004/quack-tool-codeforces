import os
import validators

from src.cli.log import Log
from src.compiler.cpp_compiler import CPPCompiler
from src.utilities.utility import Utility


class Cli:
    def __init__(self):
        self.log = Log()
        self.url = ""
        self.compiler = None
        self.running = True

    def initialize_compiler(self):
        self.set_compiler()
        self.set_samples()
        self.set_file()

    def run(self):
        self.initialize_compiler()

        while self.running:
            self.print_commands()
            self.handle_user_commands()

        self.on_exit()

    def set_samples(self):
        is_samples_set = False

        while not is_samples_set:
            url = input("What is the problem URL: ")

            if not validators.url(url):
                print("This is an invalid URL, try again\n")
                continue

            self.compiler.set_samples(Utility.get_samples(url))
            is_samples_set = True

    def set_compiler(self):
        self.log.log_compiler_options()
        compiler_input = int(input("What extension is your file: "))

        match compiler_input:
            case 0:
                self.compiler = CPPCompiler()
            case _:
                print("Input not recognized, try again\n")

    def set_file(self):
        is_filepath_set = False
        files_in_current_directory = os.listdir()

        while not is_filepath_set:
            file = input("What is the name of your file: ")

            if file not in files_in_current_directory:
                print(f'Filename "{file}" not recognized, try again.\n')
                continue

            self.compiler.set_file(file)
            is_filepath_set = True

    def on_exit(self):
        print("Successfully exited out of Quack Tools")

    def handle_user_commands(self):
        user_input = int(input("What would you like to do: "))

        match user_input:
            case 0:
                self.compiler.compile()
            case 1:
                self.compiler.get_program_output()
            case 2:
                self.compiler.test_samples_with_user_output()
            case _:
                self.running = False

    def print_commands(self):
        print("lol")
