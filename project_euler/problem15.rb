def factorial(num)
  if num == 0
  	1
  else
    num * factorial(num-1)
  end
end

def combination(size_of_grid)
  factorial(size_of_grid * 2) / (factorial(size_of_grid) * factorial(size_of_grid))
    
end

p combination(20)
