import subprocess

from quacktools.compiler.compiler import Compiler


class CPPCompiler(Compiler):
    def __init__(self, app):
        super().__init__(app)
        self.executable_file = ""

    def compile(self):
        self.executable_file = self.filename + ".exe"
        command = f"g++ {self.file} -o {self.executable_file}"
        subprocess.run(command, check=True, shell=True)

        # Display compilation errors to user

    def get_program_output(self):
        user_outputs = []

        for sample_input in self.samples["input"]:
            sample_input = "".join(sample_input).strip()
            command = f"./{self.executable_file}"

            with open("output.txt", "w", encoding="utf-8") as output_file:
                subprocess.run(
                    command,
                    check=True,
                    stdout=output_file,
                    input=sample_input.encode(),
                    stderr=subprocess.PIPE,
                )

            with open("output.txt", "r", encoding="utf-8") as output_file:
                user_outputs.append(output_file.read())

        self.user_outputs = user_outputs
