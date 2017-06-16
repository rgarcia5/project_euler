def is_prime?(num)
  i = 2
  while i <= Math.sqrt(num)
  return false if num % i == 0
    i += 1
  end
  return true
end

def ten_thousand_first_prime
  i = 3
  count = 0
  while true
    if is_prime?(i)
      count += 1
    end
    break if count == 10_000
  	i += 2
  end
  i

end

p ten_thousand_first_prime
