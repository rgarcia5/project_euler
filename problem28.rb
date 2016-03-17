def squares(num)
  num ** 2
end

def number_spiral_diagonals(length)
  sum = 1
  (3..length).to_a.each do |number|
  	if number.odd?
      sum += squares(number)
      i = 1
      while i < 4
        sum += (squares(number) - ((number - 1) * i))
        i += 1
      end
    end
  end

  sum

end

p number_spiral_diagonals(1001)