def is_palindrome?(num)
  i = 0
  number_string = num.to_s
  while i < number_string.length
    if num[i] == num[num.length-1-i]
    	return false
    end
  end
  return true
end

def products
 palindromes = []
 
 i = 100
 while i < 1000
  j = 100
  while j < 1000
    if is_palindrome?(i*j)
    	palindrome << i*j
    end
  	j += 1
  end
 	i += 1
 end

 palindrome.max
end