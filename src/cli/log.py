from prettytable import PrettyTable
from src.constants.table_constants import TEST_CASE_OUTPUT_COLUMNS


class Log:
    @staticmethod
    def log_test_case_output(iteration, test_case_output):
        table = PrettyTable(TEST_CASE_OUTPUT_COLUMNS)
        table.align["INPUT"] = "l"
        test_case_output.insert(0, str(iteration))
        test_case_output.append("AC")
        table.add_row(test_case_output)

        print(table)
