# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import sys
sys.path.append('/Users/danielshin/Documents/turing/other/python/event_reporter_python/lib')
import session

class SessionTest(unittest.TestCase):

    def test_session_isolates_command_from_input(self):
        s = session.Session()

        s.execute_command("load")
        self.assertEqual(s.command, "load")

        s.execute_command("find first_name danny")
        self.assertEqual(s.command, "find")

        s.execute_command("queue print")
        self.assertEqual(s.command, "queue")

        s.execute_command("help load")
        self.assertEqual(s.command, "help")

        s.execute_command("load test.csv")
        self.assertEqual(s.command, "load")

    def test_session_isolates_parameters_from_input(self):
        s = session.Session()

        s.execute_command("load test_file.csv")
        self.assertEqual(s.params, ["test_file.csv"])

        s.execute_command("find first_name Allison")
        self.assertEqual(s.params, ["first_name", "Allison"])

        s.execute_command("queue print")
        self.assertEqual(s.params, ["print"])

        s.execute_command("queue print by last_name")
        self.assertEqual(s.params, ["print by", "last_name"])

        s.execute_command("help")
        self.assertEqual(s.params, None)

        s.execute_command("help print_by")
        self.assertEqual(s.params, "print_by")

        s.execute_command("queue export html test.html")
        self.assertEqual(s.params, ["export html", "test.html"])


if __name__ == '__main__':
    unittest.main()
