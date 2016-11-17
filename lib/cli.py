import sys
sys.path.append('/Users/danielshin/Documents/turing/other/python/event_reporter_python/lib')

class CLI:
    def __init__(self):
        self.command = ''
        self.input = None
        self.exit_commands = ["q", "quit", "exit", "e"]

    def execute(self):
        print("Intro")

        while True:
            self.command = raw_input("Enter Something\n")

            if self.command not in self.exit_commands:
                continue
            else:
                print("Good bye")
                break
