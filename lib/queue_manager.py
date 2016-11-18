import sys
sys.path.append('/Users/danielshin/Documents/turing/other/python/event_reporter_python/lib')
import csv_manager as cm
from pdb import set_trace as bp

class QueueManager:

    def __init__(self):
        self.queue = []

    def queue_add(self, results):
        if type(results) is list:
            self.queue = results
        else:
            self.queue = [results]
        return self.queue

        print("Queue added")

    def queue_count(self):
        return len(self.queue)

    def queue_clear(self):
        self.queue = []
        print("Queue cleared")
