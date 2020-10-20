#Author: Tow 10/19/2020

year = int(input('Enter the year'))
month = int(input('Enter the month'))
day = int(input('Enter the day'))

if month == 1:
    month = month + 12
    year = year - 1
elif month == 2:
    month = month + 12
    year = year - 1

century = (year // 100)
century_year = (year % 100)

day_of_week = (day + ((26 * (month + 1)) // (10)) + century_year + ((century_year) // \
    (4)) + ((century) // (4)) + (5 * century)) % 7

if day_of_week == 0:
    print( 'Day of week is a Saturday')
elif day_of_week == 1:
    print('Day of the week is a Sunday')
elif day_of_week == 2:
    print( 'Day of the week is a Monday')
elif day_of_week == 3:
    print('Day of the week is a Tuesday')
elif day_of_week == 4:
    print('Day of the week is a Wednesday')
elif day_of_week == 5:
    print('Day of the week is a Thursday')
elif day_of_week == 6:
    print('Day of the week is a Friday')

 # print( '\n' + '\' str(month) + '\'  str(day) '\'  + str(year) + 'was a Saturday'    