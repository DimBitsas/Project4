import datetime
DATE_PROMPT = "Enter the date\nPlease use YYYY-MM-DD: "


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

