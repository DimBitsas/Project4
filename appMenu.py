import os
import sys
import time
from task import add_task
from task import init_task_db
from task import task_search_name

MAIN_MENU = "WORK_LOG\na) Add new entry\nb) Search in existing entries\nc) Quit program"
SEARCH = "\nDo you want to search by: \na) Find by employee name\nb) " \
"Find by date\nc) Find by time spent\nd) Find by search term\ne) Return to menu\n\n"
TRY_AGAIN = "Please provide a valid input\nTry again!!\n\n"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def tasks_search():
    """Provide/Choose search type
       Show search results
    """
    while True:
        clear_screen()
        user_input = input(SEARCH).upper()
        if user_input == 'E':
            return
        elif user_input == 'A':
            task_search_name("nikos")
        elif user_input == 'B':
            print("date search")
        elif user_input == 'C':
            print("time serach")
        elif user_input == 'D':
            print("teram search")
        else:
            print(TRY_AGAIN)

def app_menu():
    """Application menu"""
    init_task_db()
    while True:
        clear_screen()
        prompt_res = input(MAIN_MENU).upper()
        if prompt_res == 'A':
            add_task()
        elif prompt_res == 'B':
            tasks_search()
        elif prompt_res == 'C':
            sys.exit()
        else:
            print("Error: Please provide a valid input: a,b or c\n\n")
            time.sleep(4)


if __name__ == '__main__':
    app_menu()