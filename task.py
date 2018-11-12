from peewee import *
from task_time import task_minutes
from dates_handler import get_user_date


db = SqliteDatabase('task db')

NAME = "Employee name: "
TASK_NAME ="Title of the task: "
TASK_TIME = "Time spent (minutes): "
NOTES = "Notes (Optional): "

class Task(Model):
    task_date = DateField(formats=['%Y-%m-%d'])
    user_name = CharField(max_length=255)
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
    u_name = input(NAME).strip()
    t_name = input(TASK_NAME).strip()
    t_time = task_minutes()
    t_notes = input(NOTES).strip()
    
    Task.create(task_date=t_date, user_name=u_name, task_name=t_name, task_time=t_time, task_notes=t_notes )
    
results_list = []
results_dict = {}    
    
def task_search_name(emp_name):
    emp = Task.select().where(Task.user_name==emp_name)
    
    for e in emp:      
        results_dict = {'Name': e.user_name, 'Date': e.task_date, 'Time': e.task_time, 'Notes': e.task_notes}
        results_list.append(results_dict)

    for x in results_list:
        print(x)

