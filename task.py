from peewee import *
from task_time import task_minutes
from dates_handler import get_user_date

DATE_KEY = 'Date'
TASK_NAME_KEY = 'TaskName'
NAME_KEY = 'Name'
TIME_KEY = 'Time'
NOTES_KEY = 'Notes'

NAME = "Employee name: "
TASK_NAME ="Title of the task: "
NOTES = "Notes (Optional): "
TERM = "Search term: "

db = SqliteDatabase('task db')

results_list = []
results_dict = {}

class Task(Model):
    task_date = DateField(formats=['%Y-%m-%d'])
    employee_name = CharField(max_length=255)
    task_name = CharField(max_length=255)
    task_time = FloatField(default=0)
    task_notes = TextField()
    
    class Meta:
        database = db

def init_task_db():
    db.connect()
    db.create_tables([Task], safe=True)
        
def add_task():
    t_date = get_user_date()
    e_name = input(NAME).strip()
    t_name = input(TASK_NAME).strip()
    t_time = task_minutes()
    t_notes = input(NOTES).strip()
    
    Task.create(task_date=t_date, employee_name=e_name, task_name=t_name, task_time=t_time, task_notes=t_notes )
    
def clear_results_list():
    results_list.clear()

def show_emp():
    emp = Task.select()
    emp_list = []
    
    for i in emp:
        if i.employee_name not in emp_list:
            emp_list.append(i.employee_name)
    
    for i in emp_list:
        print(i, " ", end='')
    print("\n")
    
def show_dates():
    dates = Task.select()
    dates_list = []
    
    for i in dates:
        if i.task_date not in dates_list:
            dates_list.append(i.task_date)
    
    for i in dates_list:
        print(i, " ", end='')
    print("\n")

def show_search_results():
    """Show to the user the search results in a appropriate format"""
    if len(results_list) == 0:
        print("None task found!!\n")
        return
    for i in results_list:
        print("\n")
        print("Date:           ", i[DATE_KEY])
        print("Employee name:  ", i[NAME_KEY])
        print("Task name:      ", i[TASK_NAME_KEY])
        print("Time Spent:     ", i[TIME_KEY])
        print("Notes:          ", i[NOTES_KEY])
        print("\nResult        ", results_list.index(i)+1, "of", len(results_list), "\n")
        user_input = input("Enter R             --> Back to search menu\nEnter any other key --> Next task\n").upper()
        if user_input == 'R':
            return
    
def append_to_result_list(res):
    for i in res:      
        results_dict = {DATE_KEY: i.task_date, NAME_KEY: i.employee_name, 
                        TASK_NAME_KEY: i.task_name, TIME_KEY: i.task_time, NOTES_KEY: i.task_notes}
        results_list.append(results_dict)    
        
def search_task_by_emp():
    emp_name = input(NAME)
    emp = Task.select().where(Task.employee_name==emp_name)    
    append_to_result_list(emp)

def search_task_by_date():
    tdate = get_user_date()
    dates = Task.select().where(Task.task_date==tdate)
    append_to_result_list(dates)          
        
def search_task_by_time():
    user_time = task_minutes()    
    times_res = Task.select().where(Task.task_time==user_time)
    append_to_result_list(times_res)
    
def search_task_by_term():
    sterm = input(TERM)
    res = Task.select().where(Task.task_name.contains(sterm) | Task.task_notes.contains(sterm) )
    append_to_result_list(res)
    
def search_task_by_date_range():
    print("First date")
    tdate1 = get_user_date()
    print("Second date")
    tdate2 = get_user_date()
    
    tmp = tdate1
    if tdate1 > tdate2:
        tdate1 = tdate2
        tdate2 = tmp
    
    dates = Task.select().where(Task.task_date> tdate1, Task.task_date < tdate2)
    append_to_result_list(dates)