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
    l = []
    for i in range(-k[0], kDay):
        if i < 0:
            l.append(0)
        elif i < 9:
            l.append(i + 1)
            #s += '0' + str(i + 1) + ' '
        else:
            l.append(i + 1)
            #s += str(i +1) + ' '
    for i in range(0, len(l)):
        if i > 0 and i % 7 == 0:
            s = s.rstrip()
            s += '\n'
        if l[i] == 0:
            s += '   '
        elif l[i] <= 9:
            s += '0' + str(i - k[0] + 1) + ' '
        else:
            s += str(i - k[0] + 1) + ' '
    s = s.rstrip()
    return res + s
print create_calendar_page(3)

