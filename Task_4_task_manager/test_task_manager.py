import unittest
import task_manager as tm


class TaskManagerTestCase(unittest.TestCase):

    def setUp(self):
        self.task_manager = tm.TaskManager()

    def test_create_task(self):
        self.task_manager.create_task('task_1', 'description')
        result = self.task_manager.get_tasks_by_id(1)
        expected = tm.Task(1, 'task_1', 'description', 'IN PROCESS')

        self.assertEqual(result.get_task_values(),
                         expected.get_task_values())

    def test_update_status(self):
        self.task_manager.create_task('task_2', 'description')
        self.task_manager.update_status(self.task_manager.tasks[1])
        result = self.task_manager.get_tasks_by_id(1).status
        expected = 'DONE'
        self.assertEqual(result, expected)

    def test_remove_task_by_id(self):
        result = self.task_manager.remove_task_by_id(5)
        expected = "There are no tasks with the specified id"
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
