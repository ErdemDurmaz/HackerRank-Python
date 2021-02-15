def is_leap(year):
    leap = False
    if year % 4 ==0:
        if year % 100 == 0:
            if year /4 == 0:
                return True
        
    # Write your logic here
    
    return leap

year = int(input())