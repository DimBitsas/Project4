import datetime

DATE_PROMPT = "Enter the date\nPlease use YYYY-MM-DD: "
TASK_TIME = "Time Spent (minutes): "

DATE_KEY = 'Date'
TASK_NAME_KEY = 'TaskName'
NAME_KEY = 'Name'
TIME_KEY = 'Time'
NOTES_KEY = 'Notes'

NAME = "Employee name: "
TASK_NAME = "Title of the task: "
NOTES = "Notes (Optional): "
TERM = "Search term: "

EDIT_PROMPT = "a) Edit employee name\nb) Edit date\nc) Edit time\nd) Edit notes\ne) Edit task name"


def get_search_term():
    """Prompt user for search term"""
    term = ""
    while len(term) == 0:
        term = input(TERM)
    return term


def get_emp_name():
    """Prompt user for employee name"""
    emp_name = ""
    while len(emp_name) == 0:
        emp_name = input(NAME)
    return emp_name


def get_user_date():
    """Ask user for a date of a specific format
       Return date
    """
    while True:
        date = input(DATE_PROMPT)
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            print("{0}: does not seem to be a valid date\n".format(date))
            continue
        else:
            return date


def task_minutes():
    """Prompt user for task time and return user input"""
    while True:
        time_input = input(TASK_TIME)
        try:
            float(time_input)
        except ValueError:
            print("Please provide a numeric value\n")
            continue
        return float(time_input)
