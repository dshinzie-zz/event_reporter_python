import sys
sys.path.append('/Users/danielshin/Documents/turing/other/python/event_reporter_python/lib')
import csv_manager as cm

class Session:

    def __init__(self):
        self.manager = cm.CSVManager()
        self.qm = None
        self.help = None

    def execute_command(self, command):
        self.command, self.params = self.split_parameters(command)


    def split_parameters(self, input):
        output = input.split()
        if len(output) == 1:
            return [output[0].lower(), None]
        elif output[0] == "help":
            return [output[0].lower(), ''.join(output[1:])]
        elif len(output) == 2:
            return [output[0].lower(), [output[1].lower()]]
        elif output[0] == "queue" and len(output) > 2:
            return [output[0].lower(), [' '.join(output[1:3]), output[3]]]
        elif output[0] == "find":
            return [output[0].lower(), [output[1], ' '.join(output[2:])]]
