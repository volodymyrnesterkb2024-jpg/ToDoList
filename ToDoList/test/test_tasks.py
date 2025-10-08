import unittest
from ToDoList.tasks import Task
from ToDoList.utils import find_task_by_id, get_next_id, validate_priority

class TestTask(unittest.TestCase):
    # код тестів без змін
    def test_create_task(self):
        task = Task(1, "Test")
        self.assertEqual(task.title, "Test")
        self.assertFalse(task.completed)
        self.assertEqual(task.priority, "medium")
    
    def test_create_task_with_priority(self):
        task = Task(1, "High Priority Task", priority="high")
        self.assertEqual(task.priority, "high")
    
    def test_task_completion(self):
        task = Task(1, "Test")
        task.completed = True
        self.assertTrue(task.completed)

class TestUtils(unittest.TestCase):
    def setUp(self):
        self.tasks = [
            Task(1, "First", completed=False),
            Task(2, "Second", completed=True),
            Task(3, "Third", completed=False)
        ]
    
    def test_find_task_by_id(self):
        task = find_task_by_id(self.tasks, 2)
        self.assertIsNotNone(task)
        self.assertEqual(task.title, "Second")
    
    def test_find_nonexistent_task(self):
        task = find_task_by_id(self.tasks, 99)
        self.assertIsNone(task)
    
    def test_get_next_id(self):
        next_id = get_next_id(self.tasks)
        self.assertEqual(next_id, 4)
    
    def test_get_next_id_empty_list(self):
        next_id = get_next_id([])
        self.assertEqual(next_id, 1)
    
    def test_validate_priority(self):
        self.assertTrue(validate_priority("low"))
        self.assertTrue(validate_priority("medium"))
        self.assertTrue(validate_priority("high"))
        self.assertTrue(validate_priority("HIGH"))
        self.assertFalse(validate_priority("invalid"))

if __name__ == "__main__":
    unittest.main()