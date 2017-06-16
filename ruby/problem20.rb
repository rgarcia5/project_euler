def factorial(num)
  result = 1
  i = num
  while i > 0
    result *= i

  	i -= 1
  end
 result
end

def sum(num)
  num.to_s.split("").map{|num| num.to_i}.inject(0){|sum,num| sum += num}


end

p sum(factorial(100))
