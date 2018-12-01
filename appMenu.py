import sys
import time
from task import add_task, init_task_db, db
from task_search import EmpSearch, DateSearch, TimeSearch, TermSearch, DateRangeSearch
from task_search import create_result_list, show_results, reset_results, clear_screen
from prompts import *

MAIN_MENU = "WORK_LOG\na) Add new entry\nb) Search in existing entries\nc) Quit program"
SEARCH = "SEARCH MENU: \na) Find by employee name\nb) " \
"Find by date\nc) Find by time spent\nd) Find by search term\ne) Find by range of dates\nf) Return to menu\n\n"
TRY_AGAIN = "Please provide a valid input\nTry again!!\n\n"

 
def tasks_search():
    """Provide/Choose search type
       Show search results
    """
    while True:
        clear_screen()
        user_input = input(SEARCH).upper()
        clear_screen()
        if user_input == 'F':
            return None
        elif user_input == 'A':
            res = EmpSearch().search()
        elif user_input == 'B':
            res = DateSearch().search()
        elif user_input == 'C':
            res = TimeSearch().search()
        elif user_input == 'D':
            res = TermSearch().search()
        elif user_input == 'E':
            res = DateRangeSearch().search()
        else:
            print(TRY_AGAIN)
            continue
        create_result_list(res)
        show_results()
        reset_results()

def app_menu():
    """Application menu"""
    init_task_db()
    while True:
        clear_screen()
        prompt_res = input(MAIN_MENU).upper()
        clear_screen()
        if prompt_res == 'A':
            add_task(get_user_date(), get_emp_name().strip(), input(TASK_NAME).strip(), task_minutes(), input(NOTES).strip() )
        elif prompt_res == 'B':
            tasks_search()
        elif prompt_res == 'C':
            db.close()
            return None
        else:
            print("Error: Please provide a valid input: a,b or c\n\n")
            time.sleep(4)


if __name__ == '__main__':
    app_menu()
    sys.exit()
