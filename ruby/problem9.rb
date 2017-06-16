def pythagorean_formula(a,b)
  Math.hypot(a,b)

end

def triplet
  i = 2
  while i < 500
    j = 2
    while j < 500
      hypotenuse = pythagorean_formula(i,j)

      if hypotenuse% 1 == 0
       sum = i +j + hypotenuse
       return i*j*hypotenuse if sum == 1000
      end
      j += 1
    end
   i += 1
  end
  
end

p triplet
