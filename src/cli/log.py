from prettytable import PrettyTable, ALL
from src.constants.table_constants import TEST_CASE_OUTPUT_COLUMNS


class Log:
    @staticmethod
    def log_compiler_options():
        pass

    @staticmethod
    def log_custom_table(headers, rows, testing=False):
        table = PrettyTable(headers)
        table.add_rows(rows)
        table.hrules = ALL
        table.align = "l"

        print(table)
