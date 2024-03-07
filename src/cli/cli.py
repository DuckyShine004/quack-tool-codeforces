from src.cli.log import Log


class Cli:
    def __init__(self):
        self.log = Log()
        self.running = True

    def run(self):
        while self.running:
            self.print_commands()
            self.handle_user_commands()

        self.on_exit()

    def on_exit(self):
        print("Successfully exited out of Quack Tools")

    def handle_user_commands(self):
        user_input = int(input("Enter a number: "))

        match user_input:
            case 0:
                self.running = False
            case _:
                self.running = False

    def print_commands(self):
        print("lol")
