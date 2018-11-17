import datetime

DATE_PROMPT = "Enter the date\nPlease use YYYY-MM-DD: "
TASK_TIME = "Time Spent (minutes): "

DATE_KEY = 'Date'
TASK_NAME_KEY = 'TaskName'
NAME_KEY = 'Name'
TIME_KEY = 'Time'
NOTES_KEY = 'Notes'

NAME = "Employee name: "
TASK_NAME ="Title of the task: "
NOTES = "Notes (Optional): "
TERM = "Search term: "

def get_user_date():
    """Ask user for a date of a specific format
       Return date
    """
    while True:
        date_input = ""
        try:
            date_input = input(DATE_PROMPT)
            date = datetime.datetime.strptime(date_input, '%Y-%m-%d').date()
        except ValueError:
            print("Error: {0}: does not seem to be a valid date\n".format(date_input))
            continue
        else:
            break
    return date

def task_minutes():
    """Prompt user for task time and return user input"""
    while True:
        time_input = input(TASK_TIME)
        try:
            float(time_input)
        except ValueError:
            print("Error: Please provide a numeric value\n")
            continue
        return float(time_input)

