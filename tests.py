import unittest
from unittest.mock import patch
import unittest.mock as mock

import appMenu
import task
from task import Task
import task_search
import prompts
from prompts import *


class TestTask(unittest.TestCase):
    def setUp(self):
        self.test_tdate = "2006-10-10"
        self.test_ename = "somebody"
        self.test_tname = "test task"
        self.test_ttime = "10"
        self.test_tnotes = "test notes"
        self.test_task = task.add_task(self.test_tdate, self.test_ename, self.test_tname, self.test_ttime, self.test_tnotes)
         
    def test_add_task(self):
        self.assertEqual(self.test_task.task_date, self.test_tdate )
        
    def tearDown(self):
        task.Task.delete().where(task.Task.task_date==self.test_tdate, task.Task.employee_name==self.test_ename, 
                                 task.Task.task_name==self.test_tname, task.Task.task_time==self.test_ttime, 
                                 task.Task.task_notes==self.test_tnotes).execute()

class TestSearch(unittest.TestCase):
    
    def setUp(self):
        self.test_tdate = "1000-10-10"
        self.test_ename = "test_name"
        self.test_tname = "test_task"
        self.test_ttime = "50"
        self.test_tnotes = "test_notes"
        self.test_task = task.add_task(self.test_tdate, self.test_ename, self.test_tname, self.test_ttime, self.test_tnotes)
        
    def tearDown(self):
        task.Task.delete().where(task.Task.task_date==self.test_tdate, task.Task.employee_name==self.test_ename, 
                                 task.Task.task_name==self.test_tname, task.Task.task_time==self.test_ttime, 
                                 task.Task.task_notes==self.test_tnotes).execute()
        
    def test_create_result_list(self):
        res = Task.select().where(Task.employee_name==self.test_ename)
        self.assertEqual(task_search.create_result_list(res), 1)
    
    def test_show_results_del(self):
        res = Task.select().where(Task.employee_name==self.test_ename)
        task_search.reset_results()
        task_search.create_result_list(res)
        with patch('builtins.input', side_effect=['D']):
            self.assertEqual(task_search.show_results(), 0)
    
    def test_show_results_return(self):
        res = Task.select().where(Task.employee_name==self.test_ename)
        task_search.reset_results()
        task_search.create_result_list(res)
        with patch('builtins.input', side_effect=['R']):
            self.assertEqual(task_search.show_results(), 1)
    
    def test_show_results_none_found(self):
        task_search.reset_results()
        self.assertEqual(task_search.show_results(), 0)
    
    def test_emp_search(self):
        with patch('builtins.input', side_effect=[self.test_ename]):
            res = task_search.EmpSearch().search()
            task_search.reset_results()
            self.assertEqual(task_search.create_result_list(res), 1)
    
    def test_date_search(self):
        with patch('builtins.input', side_effect=[self.test_tdate]):
            res = task_search.DateSearch().search()
            task_search.reset_results()
            self.assertEqual(task_search.create_result_list(res), 1)
            
    def test_time_search(self):
        with patch('builtins.input', side_effect=[self.test_ttime]):
            res = task_search.TimeSearch().search()
            task_search.reset_results()
            self.assertEqual(task_search.create_result_list(res), 1)
    
    def test_term_search(self):
        with patch('builtins.input', side_effect=['test']):
            res = task_search.TermSearch().search()
            task_search.reset_results()
            self.assertEqual(task_search.create_result_list(res), 1)
            
    def test_date_range_search(self):
        with patch('builtins.input', side_effect=['1000-01-01', '1990-10-11']):
            res = task_search.DateRangeSearch().search()
            task_search.reset_results()
            self.assertEqual(task_search.create_result_list(res), 1)

class TestPrompts(unittest.TestCase):

    def test_valid_time(self):
        with patch('builtins.input', side_effect=['40']):
            self.assertEqual(prompts.task_minutes(), 40)
     
    def test_invalid_time(self):
        with mock.patch('builtins.input', side_effect=["40a", 40],
            return_value=40):
            self.assertRaises(ValueError)
            assert prompts.task_minutes() == 40

    def test_valid_date(self):
        with patch('builtins.input', side_effect=['1998-10-10']):
            self.assertEqual(prompts.get_user_date(), '1998-10-10')

    def test_invalid_date(self):
        with mock.patch('builtins.input',
            side_effect=["1998/10/10", "1998-10-10"],
            return_value="1998-10-10"):
            self.assertRaises(ValueError)
            assert prompts.get_user_date() == "1998-10-10"
            
    def test_get_emp_name(self):
        with patch('builtins.input', side_effect=['George']):
            self.assertEqual(prompts.get_emp_name(), 'George')
            
    def test_get_search_term(self):
        with patch('builtins.input', side_effect=['some term']):
            self.assertEqual(prompts.get_search_term(), 'some term')
    
class TestAppMenu(unittest.TestCase):
    
    def test_tasks_search_F(self):
        with patch('builtins.input', side_effect=['F']):
            self.assertEqual(appMenu.tasks_search(), None)
    
    def test_app_menu_quit(self):
        with patch('builtins.input', side_effect=['C']):
            self.assertEqual(appMenu.app_menu(), None)
            

if __name__ == "__main__":
    unittest.main()
