import datetime
import calendar

def create_calendar_page(month = None,year = None):
    dt = datetime.date.today()
    if month == None:
        month = dt.month
    if year == None:
        year = dt.year
    dt = dt.replace(year, month, 1)

    res = "--------------------\n" \
        "MO TU WE TH FR SA SU\n" \
        "--------------------\n"
    s = ''
    kDay = calendar.mdays[dt.month]
    k = calendar.monthrange(dt.year, dt.month)
    a = calendar.Calendar()

    return a
print create_calendar_page(1)
