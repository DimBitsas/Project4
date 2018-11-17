from peewee import *
from prompts import *

db = SqliteDatabase('task db')

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
