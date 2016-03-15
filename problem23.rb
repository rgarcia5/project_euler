
class Integer
  def is_abundant_num?
    sum = 1
    i = 2
    while i <= Math.sqrt(self)
      if self % i == 0 && i ** 2 == self
        sum += self/i
        break   
      elsif self % i == 0
        sum += self/i + i
      end
  	  i += 1
    end

    if sum > self
  	  return true
    else
      return false
    end
  end
end


def not_abundant_sum
  list = []
  i = 1
  while i < 28124
    if i.is_abundant_num?
      list << i
    end
    
  	i += 1
  end
 
  sums = []
  list.each do |first_num|
    list.each do |second_num|
      if first_num + second_num > 28123
        break
      else
        sums << first_num + second_num
      end
    end
  end
 
  ((1..28123).to_a - sums).reduce(:+)
 
end

p not_abundant_sum

