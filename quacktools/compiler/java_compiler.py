import subprocess

from quacktools.compiler.compiler import Compiler


class JavaCompiler(Compiler):
    def __init__(self, app):
        super().__init__(app)

    def compile(self):
        command = f"javac {self.file}"
        subprocess.run(command, check=True, shell=True)

    def get_program_output(self) -> None:
        """Get the user's program's code output."""

        command = f"java {self.filename}"

        for sample_input in self.samples["input"]:
            sample_input = "".join(sample_input).strip()
            self.get_user_output(sample_input, command)
