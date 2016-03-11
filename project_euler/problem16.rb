def sum_of_digits(num)
  ary = (2 ** num).to_s.split("").map{|num| num.to_i}
  ary.inject(0) { |sum, num| sum += num}
end



p sum_of_digits(1000)