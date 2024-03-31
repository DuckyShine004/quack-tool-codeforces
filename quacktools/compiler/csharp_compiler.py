import os
import subprocess

from quacktools.compiler.compiler import Compiler


class CsharpCompiler(Compiler):
    def __init__(self, app):
        super().__init__(app)

    def compile(self):
        command = f"cd {self.filename} && dotnet build"
        subprocess.run(command, check=True, shell=True)

    def get_program_output(self) -> None:
        """Get the user's program's code output."""

        command = f"cd {self.filename} && dotnet run"

        for sample_input in self.samples["input"]:
            sample_input = "".join(sample_input).strip()
            self.get_user_output(sample_input, command)
