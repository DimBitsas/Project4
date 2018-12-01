from peewee import *

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
    """Connect to the database"""
    db.connect()
    db.create_tables([Task], safe=True)
        
def add_task(t_date, e_name, t_name, t_time, t_notes):
    """Add new task"""
    return Task.create(task_date=t_date, employee_name=e_name, task_name=t_name, task_time=t_time, task_notes=t_notes )
