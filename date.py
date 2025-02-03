import datetime as dt

def get_current_date():

    # use the date time library to get the current date
    date = dt.date.today()
    # print(date)
    return date

if __name__ == "__main__":
    get_current_date()