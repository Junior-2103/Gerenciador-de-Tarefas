from task_manager import TaskManager
import unittest
import os

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager('project/test_tasks.json')
        self.manager.tasks = []
    def tearDown(self):
        if os.path.exists('project/test_tasks.json'):
            os.remove('project/test_tasks.json')

    def test_create_task(self):
        task_id = self.manager.add_task('Title','Description','pendente')
        task = self.manager.get_task(task_id)
        self.assertEqual(task['title'],'Title')
        self.assertEqual(task['description'],'Description')
        self.assertEqual(task['status'],'pendente')

    def test_update_non_existent_task(self):
        with self.assertRaises(ValueError):
            self.manager.modify_task('id_invalid',title='Oi')

    def test_delete_non_existent_task(self):
        with self.assertRaises(ValueError):
            self.manager.delete_task('id_invalid')

    def test_list_task_filtered(self):
        self.manager.add_task('Title1','Description1','pendente')
        self.manager.add_task('Title2','Description2','concluido')
        tasks = self.manager.list_tasks('pendente')
        self.assertEqual(tasks[0]['title'],'Title1')
        self.assertEqual(tasks[0]['description'],'Description1')
        self.assertEqual(tasks[0]['status'],'pendente')
        self.assertEqual(len(tasks),1)

if __name__ == "__main__":
    unittest.main()