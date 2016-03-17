def sum_of_fifth_powers
  result = []
  2.upto(354_294) do |num|
  	new_num = num
    num.to_s.split("").each do |digit|
      new_num -= (digit.to_i) ** 5
           

    end  

    if new_num == 0
      result << num
    end

  end

  result.reduce(:+)

end

p sum_of_fifth_powers