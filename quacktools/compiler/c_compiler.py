import subprocess

from quacktools.compiler.compiler import Compiler


class CCompiler(Compiler):
    def __init__(self, app):
        super().__init__(app)

        self.executable_file = ""

    def compile(self) -> None:
        """Compiles the user's code."""

        self.executable_file = self.filename + ".exe"
        command = f"gcc {self.file} -o {self.executable_file}"
        subprocess.run(command, check=True, shell=True)

        # Display compilation errors to user

    def get_program_output(self) -> None:
        """Get the user's program's code output."""

        command = f"./{self.executable_file}"

        for sample_input in self.samples["input"]:
            sample_input = "".join(sample_input).strip()
            self.get_user_output(sample_input, command)
