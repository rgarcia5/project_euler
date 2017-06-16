def is_prime?(num)
  i = 2
  while i <= Math.sqrt(num)
    return false if num % i == 0
    i += 1
  end
  return true
  
end

def parts(num)
  parts = [Math.sqrt(num)/4, Math.sqrt(num)/2, Math.sqrt(num) * 0.75, Math.sqrt(num)]
end

def sieve(n)
  ary = Array.new(n,true)
  i = 2
  sum = 0
 
  
    2.upto(Math.sqrt(n)) do |num1|
      0.upto(n) do |num2|
       ary[num1**2+num2*num1] = false 
            
      end
      
      i += 1
    end  
  
  ary.each_with_index do |values, idx|
   if values == true
    sum += idx
   end
  end  

  
  sum

end

def sum_of_primes(n)
  sum = 2
  i = 3
  while i <= n
    if is_prime?(i)
      sum += i
    end
    i += 2
  end

  sum


end

p sum_of_primes(2_000_000)
