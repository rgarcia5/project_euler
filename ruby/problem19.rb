

def possible_first_sundays  
  days = [1,2,3,4,5,6,7]

end

def twenty_eight_and_nine_day_month
   month = [2]
end

def thirty_day_months
  months = [4,6,9,11]
end

def thirty_one_day_months
  months = [1,3,5,7,8,10,12]
end

def leap_year?(yr)
  if yr % 4 == 0 || (yr % 100 == 0 && yr % 400 == 0)
    return true

  else
    return false
  end

end

def first_sunday_of_year(yr)
  first_sunday_idx = 5
  
  start_year = 1901

  
  while start_year < yr
    if (start_year) % 4 == 0 
      first_sunday_idx -=  2  
    else
      first_sunday_idx -= 1
    end

    if first_sunday_idx < 0 && leap_year?(start_year)
      first_sunday_idx = 7 + first_sunday_idx
    elsif first_sunday_idx < 0
      first_sunday_idx = 6
    end
    
    start_year += 1
  end
  
  possible_first_sundays[first_sunday_idx]
end


def count_sundays
count = 0
years = (1901..2000).to_a
years.each do |year|
  
  first_sunday = first_sunday_of_year(year)
 

  (1..12).to_a.each do |month|
    if first_sunday == 1
      p [month, year]
      count += 1
    end
    
    if twenty_eight_and_nine_day_month.include?(month)
      if leap_year?(year)
        while first_sunday < 30
          first_sunday += 7
        end
        first_sunday -= 29
      else
        while first_sunday < 29
          first_sunday += 7
        end
        first_sunday -= 28
      end
    elsif thirty_day_months.include?(month)
      while first_sunday < 31
        first_sunday += 7
      end
      first_sunday -= 30
    elsif thirty_one_day_months.include?(month)
      while first_sunday < 32
        first_sunday += 7
      end
      first_sunday -= 31
    end
   

  end
 

  end
count
end

p count_sundays




