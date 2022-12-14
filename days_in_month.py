import datetime   




def days_in_month( year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month
      
    Returns:
      The number of days in the input month.
    """
    if year >= datetime.MINYEAR and year < datetime.MAXYEAR:
        if month in range(1,13):
            if year % 4 == 0:
                if month in (1, 3, 5, 7, 8, 10, 12):
                    return 31
                elif month == 2:
                    return 29
                else:
                    return 30
            else:
                if month in (1, 3, 5, 7, 8, 10, 12):
                    return 31
                elif month == 2:
                    return 28
                else:
                    return 30
        else:
            return 0
    else:
        return 0
            

def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day
      
    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    correct_day = days_in_month(year, month)
    if day in range(1, correct_day + 1):
        return True
    else:
        return False
    
    
def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date
      
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is 
      before the first date.
    """
    if is_valid_date(year1, month1, day1) == True:
        if is_valid_date(year2, month2, day2) == True:
            date1=datetime.date(year1, month1, day1)
            date2=datetime.date(year2, month2, day2)
            difference=date2 - date1
            if difference.days < 1:
                return 0
            else:
                return difference.days
        else:
            return 0
    else:
        return 0
    
    
def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day
      
    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    if year == 0:
        return 0
    else:
        if day > days_in_month(year, month):
            return 0
        else:
            today= datetime.date.today()
            birthday=datetime.date(year, month, day)
            result=(days_between(birthday.year, birthday.month, birthday.day, today.year, today.month, today.day))
            return result
