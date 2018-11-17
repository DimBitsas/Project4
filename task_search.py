from task import Task
from prompts import *

class Search():
    def __init__(self):
        self.result_list = []
    
    def search(self):
        raise NotImplementedError()
    
    def append_result_list(self, res):
        """Save query results to a list of dictionaries"""
        for i in res:      
            result_dict = {DATE_KEY: i.task_date, NAME_KEY: i.employee_name, 
                           TASK_NAME_KEY: i.task_name, TIME_KEY: i.task_time, NOTES_KEY: i.task_notes}
            self.result_list.append(result_dict)
    
    def show_results(self):
        """Show to the user the search results in a appropriate format"""
        if len(self.result_list) == 0:
            print("None task found!!\n")
            return
        for i in self.result_list:
            print("\n")
            print("Date:           ", i[DATE_KEY])
            print("Employee name:  ", i[NAME_KEY])
            print("Task name:      ", i[TASK_NAME_KEY])
            print("Time Spent:     ", i[TIME_KEY])
            print("Notes:          ", i[NOTES_KEY])
            print("\nResult        ", self.result_list.index(i)+1, "of", len(self.result_list), "\n")
            user_input = input("Enter R             --> Back to search menu\nEnter any other key --> Next task\n").upper()
            if user_input == 'R':
                return
    
class EmpSearch(Search):
    def __init__(self):
        super().__init__()
        self.show_emp()
        self.emp_name = input(NAME)
        
    def search(self):
        """Search task by employee name"""
        res = Task.select().where(Task.employee_name==self.emp_name)
        super(EmpSearch, self).append_result_list(res)
        super(EmpSearch, self).show_results()
        
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
        
class DateSearch(Search):
    def __init__(self):
        super().__init__()
        self.show_dates()
        self.tdate = get_user_date()
    
    def search(self):
        """Search task by date"""
        res = Task.select().where(Task.task_date==self.tdate)
        super(DateSearch, self).append_result_list(res)
        super(DateSearch, self).show_results()
        
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
            
class TimeSearch(Search):
    def __init__(self):
        super().__init__()
        self.ttime = task_minutes()
        
    def search(self):
        """Search task by time"""
        res =Task.select().where(Task.task_time==self.ttime)
        super(TimeSearch, self).append_result_list(res)
        super(TimeSearch, self).show_results()
        
class TermSearch(Search):
    def __init__(self):
        super().__init__()
        self.term = input(TERM)
    
    def search(self):
        """Search by term"""
        res = Task.select().where(Task.task_name.contains(self.term) | Task.task_notes.contains(self.term) )
        super(TermSearch, self).append_result_list(res)
        super(TermSearch, self).show_results()
        
class DateRangeSearch(Search):
    def __init__(self):
        super().__init__()
        self.tdate1 = get_user_date()
        self.tdate2 = get_user_date()
        if self.tdate1 > self.tdate2:
            self.tdate1, self.tdate2 = self.tdate2, self.tdate1

    def search(self):
        """Search by date range"""
        res = Task.select().where(Task.task_date> self.tdate1, Task.task_date < self.tdate2)
        super(DateRangeSearch, self).append_result_list(res)
        super(DateRangeSearch, self).show_results()
        