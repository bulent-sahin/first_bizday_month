#!/usr/bin/env python3
"""
  first_bizday_month.py
  * trying to find the first business day of the month...
  21 july 2020 --- bulent0sahin@gmail.com
  27 july 2020 <--- some git updates
"""

import sys
import calendar
import datetime
import holidays

def main():
    """
      main method
    """
    year = datetime.date.today().year
    month = datetime.date.today().month
    if len(sys.argv) == 3:
        year = int(sys.argv[1])
        month = int(sys.argv[2])

    day_name = list(calendar.day_name)
    tr_holidays = holidays.Turkey(years=year)
    first_day = 1
    my_date = str(year)+"-"+str(month)+"-"+str(first_day)

    while my_date in tr_holidays:
        first_day += 1
        my_date = str(year)+"-"+str(month)+"-"+str(first_day)

    my_realdate = datetime.datetime.strptime(my_date, '%Y-%m-%d')
    while my_realdate.weekday() > 4:
        my_realdate += datetime.timedelta(days=1)

    week_day = my_realdate.weekday()
    print("the first business day of the month:", day_name[week_day],\
           my_realdate.strftime("%d-%m-%Y"))
    print("use: first_bizday_month.py <year> <month>")
    return 0


if __name__ == "__main__":
    main()
