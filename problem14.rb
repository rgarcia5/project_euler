def collatz_sequence(num)
  result = num
  count = 0
  until result == 1
    if result % 2 == 0
      result = result/2
    else
      result = (3*result + 1)
    end
    count += 1
  end

  count + 1
end


def iterate
  greatest_count = [nil,0]
  i = (1_000_000)
  while i > 1
   current_count = collatz_sequence(i)
   if current_count > greatest_count[1]
   	 greatest_count[0] = i
     greatest_count[1] = current_count
   end
  
   i -= 1
  end

  greatest_count[0]



end


p iterate
