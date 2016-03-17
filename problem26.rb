
def is_prime?(num)
  i = 2
  while i <= Math.sqrt(num)
    return false if num % i == 0
    i += 1
  end

  return true
end


def length_of_repeats(num)
  digits = []
  remainder = 1 % num
  digits << remainder
  loop do
    remainder *= 10
    digits << remainder %= num
    break if digits.length - digits.uniq.length > 0
  end
   
 digits.length - 1
  
end



def reciprocal_cycles
  greatest_repeats = nil
  i = 2
  while i < 1000
    if is_prime?(i)
      current_repeat = length_of_repeats(i)
      if greatest_repeats == nil || current_repeat > length_of_repeats(greatest_repeats)
        greatest_repeats = i
      end
    end
  	i += 1
  end
  greatest_repeats
end

p reciprocal_cycles