import unittest
import sys
sys.path.append('/Users/danielshin/Documents/turing/other/python/event_reporter_python/lib')
import session
import queue_manager

class QueueManagerTest(unittest.TestCase):

    def setUp(self):
        self.s = session.Session()
        self.s.execute_command("load")
        self.s.execute_command("find first_name danny")
        self.qm = self.s.qm.queue

    def test_queue_can_add_data_to_queue(self):
        q = queue_manager.QueueManager()
        q.queue_add("test")

        self.assertTrue(q.queue)

    def test_queue_can_count_queue(self):
        q = queue_manager.QueueManager()
        q.queue_add("test")

        self.assertEqual(q.queue_count(), 1)

    def test_queue_can_clear_queue(self):
        q = queue_manager.QueueManager()
        q.queue_add([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        q.queue_clear()

        self.assertFalse(q.queue)



if __name__ == '__main__':
    unittest.main()
