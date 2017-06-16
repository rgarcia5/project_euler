def possible_first_sundays():
  return range(1,8)


def thirty_day_months():
  return [4,6,9,11]

def thirty_one_day_months():
  return [1,3,5,7,8,10,12]

def is_leap_year(year):
  if (year % 4 == 0 or (year % 100 == 0 and year % 400 == 0)):
    return True
  return False

def first_sunday_of_year(year):
  first_sunday_idx = 5
  start_year = 1901
  while (start_year < year):
    if (start_year % 4 == 0):
      first_sunday_idx -= 2
    else:
      first_sunday_idx -= 1
    if ((first_sunday_of_year < 0 and is_leap_year(year)) or first_sunday_idx < 0):
      first_sunday_idx += 7
    start_year += 1
  return possible_first_sundays()[first_sunday_idx]

def count_sundays():
  count = 0
  years = range(1901, 2001)
  for year in years:
    first_sunday = first_sunday_of_year(year)
    months = range(1,13)
    for month in months:
      if (first_sunday == 1):
        count += 1
      if (month == 2):
        if (is_leap_year(year)):
          while (first_sunday < 30):
            first_sunday += 7
          first_sunday -= 29
        else:
          while (first_sunday < 29):
            first_sunday += 7
          first_sunday -= 28
      elif(month in thirty_day_months()):
        while (first_sunday < 31):
          first_sunday += 7
        first_sunday -= 30
      elif(month in thirty_one_day_months()):
       while (first_sunday < 32):
         first_sunday += 7
       first_sunday -= 31
  return count

print count_sundays()
