def fibonacci_sequence
  count = 1
  first_num = 1
  second_num = 1
  until first_num.to_s.length == 1000
  	result = first_num + second_num
    first_num = second_num
    second_num = result
    count += 1
  	
  end

  count

end

p fibonacci_sequence