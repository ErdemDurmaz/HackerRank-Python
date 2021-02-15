'''
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.

'''

def is_leap(year):
    leap = False
    if year % 4 ==0 and year % 400 ==0  and not year % 100 == 0:
        return True
    # Write your logic here
    return leap

year = int(input())