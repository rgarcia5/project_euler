

def factors(num)
  count = 0
  i = 1

  while i <= Math.sqrt(num)
    if num % i == 0
      count += 2
    end

    if count == 500
      return num
    end

    i += 1
  end

  if count < 500
  	count = 0
  end
  
end

def triangle_numbers
  sum = 0
  i = 1
  loop do
    factors(sum)
    if factors(sum) == sum && factors(sum) != 0
     return sum
     break
    end
    sum += i
    i += 1
    

  end
end


p triangle_numbers