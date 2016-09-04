def sum_of_multiples 
  i = 1
  ary = []
  while i < 1000
  	if i % 3 == 0 || i % 5 == 0
  		ary << i
  	end
  	i += 1
  end
  
  ary.inject(0) do |sum, num|
  	sum += num
  end

end
