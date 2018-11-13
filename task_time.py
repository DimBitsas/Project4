TASK_TIME = "Time Spent (minutes): "


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