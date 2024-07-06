from datetime import datetime, timedelta, date

def display_current_datetime(YYYY, MM, DD):
    current_date = datetime.now()
    print (f"Current date and time: {current_date}")
    return()

display_current_datetime("YYYY", "MM", "DD")