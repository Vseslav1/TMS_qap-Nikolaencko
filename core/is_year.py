def is_year_leap(year:int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            print(False)
        else:
            print(True)
    else:
        print(False)