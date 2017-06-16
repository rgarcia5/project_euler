

def not_divisible?(numerator)
  
  numbers = 
  numbers = (3,5,6,7,8,10,11,12,13,16,17,18,19,20).to_a
  numbers.all? do |denominator|
   numerator % denominator == 0
  end  	

end

def multiples
  i = 380
  until divisible?(i)
      
  	i += 2
  end
  i
end

def gcf(num1,num2)
  i = 1
  result = []	
  while i < num2
    result << i if num2%i == 0
  	i += 1
  end

result.last

end

def least_common_multiple(numbers)
 
  i = 0
  j = 1
  result = []
  while j <= numbers.length
   result << numbers[i] * numbers[j]/gcf(numbers[i],numbers[j])

   i += 1
   j += 1
  end

  until result.length > 1
    least_common_multiple(result)
    break if result.length == 1

  end

end

