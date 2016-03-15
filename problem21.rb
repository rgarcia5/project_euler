
def is_prime?(num)
  i = 2
  while i <= Math.sqrt(num)
  	return false if num % i == 0
    i += 1 
  end
  return true
end

def sum_divisors(num)
  i = 1
  sum = 1
  while i <= Math.sqrt(num)
    if num % i == 0 && (num / i) != num
      sum += (num / i) + i
    end
    i += 1
  end
  sum
end

def list_of_divisor_sums 
  sum = 0
  list_of_sums = {}  
  1.upto(10000) do |num|
    next if is_prime?(num)
     if list_of_sums[sum_divisors(num)]== num && list_of_sums != {} 
      sum += num + sum_divisors(num)
     else
      list_of_sums[num] = sum_divisors(num)
    end
  end
 sum 
end

p list_of_divisor_sums

