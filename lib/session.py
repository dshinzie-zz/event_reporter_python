import sys
sys.path.append('/Users/danielshin/Documents/turing/other/python/event_reporter_python/lib')
import csv_manager
import queue_manager
import os.path
from pdb import set_trace as bp

class Session:

    def __init__(self):
        self.manager = csv_manager.CSVManager()
        self.qm = queue_manager.QueueManager()
        self.help = None

    def execute_command(self, command):
        self.command, self.params = self.split_parameters(command)
        self.validate_commands(self.command, self.params)

        if self.command == "load":
            self.execute_load(self.params)
        elif self.command == "find":
            self.execute_find(self.params)
        elif self.command == "queue":
            self.execute_queue(self.params)
        elif self.command == "help":
            self.execute_help(self.params)

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

    def validate_commands(self, command, params):
        valid_commands = ["load", "help", "queue", "find", "exit", "e", "quit", "q"]
        valid_queue = ["count", "clear", "print", "print by", "save to", "export html", "district"]

        if self.is_invalid_command(command, valid_commands):
            print("Invalid command")
        elif command == "queue" and type(params) is list and self.is_invalid_command(params[0], valid_queue):
            print("Invalid queue")
        elif command == "queue" and type(params) is str and self.is_invalid_command(params, valid_queue):
            print("Invalid queue")
        else:
            return command, params

    def is_invalid_command(self, input, valid_list):
         return False if input in valid_list else True

    def execute_queue(self, params):
        if params[0] == "count":
            if not self.qm:
                print("Queue empty")
            else:
                print ("Queue count is %s" % self.qm.queue_count())
        elif params[0] == "clear":
            self.qm.queue_clear
        elif params[0] == "save to":
            self.manager.save_file(params[1], qm.queue)

    def execute_find(self, params):
        attributes = params[0]
        criteria = ''.join(params[1:]).lower()

        self.find(self.manager.data, attributes, criteria)

    def find(self, data, attribute, criteria):
        results = filter(lambda d: getattr(d, attribute) == criteria, data)
        self.qm.queue_add(results)

    def execute_load(self, input_filename):
        filename = self.get_filename(input_filename)

        if os.path.exists(filename):
            self.manager.load_file(filename)
            print ("File loaded")
        else:
            print("File missing")


    def get_filename(self, filename):
        if filename is None:
            filename = './event_attendees.csv'
        else:
            filename = './' + ''.join(filename)

        return filename

    def execute_help(self, params):
        pass
