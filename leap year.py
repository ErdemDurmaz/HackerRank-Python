'''
The year  divided by 4, is a leap year, unless:
The year divided by 100, it is NOT a leap year, unless: The year  divisible by 400. Then it is a leap year.
if  year is not divisible by 400 a leap year then the year divided by 100 is a leap year.


'''

def is_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)


