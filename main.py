from src.cli.cli import Cli
from src.utilities.utility import Utility

url = "https://codeforces.com/problemset/problem/1936/F"
samples = Utility.get_samples(url)
tests = Utility.get_tests(samples)


def main():
    Cli().run()


if __name__ == "__main__":
    main()
