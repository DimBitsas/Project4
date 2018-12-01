import os
import time
from task import Task
from prompts import *

result_list = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def reset_results():
    """reset results list"""
    result_list.clear()

def create_result_list(res):
    """Save query results to a list of dictionaries"""
    for i in res:      
        result_dict = {DATE_KEY: i.task_date, NAME_KEY: i.employee_name, 
                       TASK_NAME_KEY: i.task_name, TIME_KEY: i.task_time, NOTES_KEY: i.task_notes}
        result_list.append(result_dict)
    return len(result_list)
   
def show_results():
    """Show to the user the search results in a appropriate format"""
    if len(result_list) == 0:
        clear_screen()
        print("None task found!!\n")
        time.sleep(2)
        return 0

    i = 0
    while True:
        if len(result_list) == 0:
            return 0
        clear_screen()
        print("\n")
        print("Date:           ", result_list[i][DATE_KEY])
        print("Employee name:  ", result_list[i][NAME_KEY])
        print("Task name:      ", result_list[i][TASK_NAME_KEY])
        print("Time Spent:     ", result_list[i][TIME_KEY])
        print("Notes:          ", result_list[i][NOTES_KEY])
        print("\nResult        ", i+1, "of", len(result_list), "\n")
        user_input = input("Return[R],Delete[D],Edit[E],Next[N],Prev[P]\n").upper()
        task_record = Task.get(Task.task_date==result_list[i][DATE_KEY], Task.employee_name==result_list[i][NAME_KEY], 
                               Task.task_name==result_list[i][TASK_NAME_KEY], Task.task_time==result_list[i][TIME_KEY], 
                               Task.task_notes==result_list[i][NOTES_KEY])
        if user_input == 'R':
            break
        elif user_input == 'D':
            result_list.remove(result_list[i])
            task_record.delete_instance()
            if i>0:
                i-=1
        elif user_input == 'E':
            user_input = input(EDIT_PROMPT).upper()
            if user_input == 'A':
                task_record.employee_name=get_emp_name()
            elif user_input == 'B':
                task_record.task_date=get_user_date()
            elif user_input == 'C':
                task_record.task_time=task_minutes()
            elif user_input == 'D':
                task_record.task_notes=input("Notes: ")
            elif user_input == 'E': 
                task_record.task_name = input(TASK_NAME)
            else:
                continue
            result_list.remove(result_list[i])
            task_record.save()
            if i>0:
                i-=1
        elif user_input == 'P' and i>0:
            i-=1
        elif user_input == 'N' and i < len(result_list)-1:
            i+=1
        
    return len(result_list)

class EmpSearch():
    def __init__(self):
        self.show_emp()
        self.emp_name = get_emp_name()
        
    def search(self):
        """Search task by employee name"""
        return Task.select().where(Task.employee_name.contains(self.emp_name))
        
    @staticmethod          
    def show_emp():
        """Show all the employee entries"""
        emp = Task.select()
        emp_list = []
        
        for i in emp:
            if i.employee_name not in emp_list:
                emp_list.append(i.employee_name)
        
        for i in emp_list:
            print(i, " ", end='')
        print("\n")
        
class DateSearch():
    def __init__(self):
        self.show_dates()
        self.tdate = get_user_date()
    
    def search(self):
        """Search task by date"""
        return Task.select().where(Task.task_date==self.tdate)
        
    @staticmethod
    def show_dates():
        """Show all the date entries"""
        dates = Task.select()
        dates_list = []
        
        for i in dates:
            if i.task_date not in dates_list:
                dates_list.append(i.task_date)
        
        for i in dates_list:
            print(i, " ", end='')
        print("\n")
            
class TimeSearch():
    def __init__(self):
        self.ttime = task_minutes()
        
    def search(self):
        """Search task by time"""
        return Task.select().where(Task.task_time==self.ttime)
        
class TermSearch():
    def __init__(self):
        self.term = get_search_term()
    
    def search(self):
        """Search by term"""
        return Task.select().where(Task.task_name.contains(self.term) | Task.task_notes.contains(self.term) )
        
class DateRangeSearch():
    def __init__(self):
        self.tdate1 = get_user_date()
        self.tdate2 = get_user_date()
        if self.tdate1 > self.tdate2:
            self.tdate1, self.tdate2 = self.tdate2, self.tdate1

    def search(self):
        """Search by date range"""
        return Task.select().where(Task.task_date> self.tdate1, Task.task_date < self.tdate2)
