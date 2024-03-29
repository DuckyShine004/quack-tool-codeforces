import subprocess

from src.compiler.compiler import Compiler


class CPPCompiler(Compiler):
    def __init__(self):
        super().__init__()
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

            with open("output.txt", "r+") as output_file:
                subprocess.run(
                    "./" + self.executable_file,
                    check=True,
                    stdout=output_file,
                    input=sample_input.encode(),
                    stderr=subprocess.PIPE,
                )

                output_file.seek(0)
                user_outputs.append(output_file.read())

        self.user_outputs = user_outputs

    def test_samples_with_user_output(self):
        print(self.samples["output"], self.user_outputs)
