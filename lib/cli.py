import sys
sys.path.append('/Users/danielshin/Documents/turing/other/python/event_reporter_python/lib')
import session

class CLI:
    def __init__(self):
        self.session = session.Session()
        self.command = ''
        self.input = None
        self.exit_commands = ["q", "quit", "exit", "e"]

    def execute(self):
        print("Intro")

        while True:
            self.command = raw_input("Enter Something\n").strip().lower()
            if self.command not in self.exit_commands:
                self.session.execute_command(self.command)
                continue
            else:
                print("Good bye")
                break
