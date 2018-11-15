import os
import sys
import time
from task import add_task, init_task_db
from task import search_task_by_emp, search_task_by_time, search_task_by_date, search_task_by_term, search_task_by_date_range
from task import show_search_results, clear_results_list, show_emp, show_dates

MAIN_MENU = "WORK_LOG\na) Add new entry\nb) Search in existing entries\nc) Quit program"
SEARCH = "\nDo you want to search by: \na) Find by employee name\nb) " \
"Find by date\nc) Find by time spent\nd) Find by search term\ne) Find by range of dates\nf) Return to menu\n\n"
TRY_AGAIN = "Please provide a valid input\nTry again!!\n\n"


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def tasks_search():
    """Provide/Choose search type
       Show search results
    """
    while True:
        clear_screen()
        clear_results_list()
        user_input = input(SEARCH).upper()
        if user_input == 'F':
            return
        elif user_input == 'A':
            show_emp()
            search_task_by_emp()
        elif user_input == 'B':
            show_dates()
            search_task_by_date()
        elif user_input == 'C':
            search_task_by_time()
        elif user_input == 'D':
            search_task_by_term()
        elif user_input == 'E':
            search_task_by_date_range()
        else:
            print(TRY_AGAIN)
            continue
        show_search_results()

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