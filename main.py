from src.cli.cli import Cli
from src.utilities.utility import Utility
from src.cli.log import Log

url = "https://codeforces.com/problemset/problem/1936/F"
samples = Utility.get_samples(url)
inputs = samples["input"]
outputs = samples["output"]

table = ["".join(inputs[0]), "".join(outputs[0])]
Log.log_test_case_output(1, table)


def main():
    Cli().run()


if __name__ == "__main__":
    main()
