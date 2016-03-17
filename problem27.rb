require 'prime'

def quadratic_primes
  longest_count = 0
  coefficients = [nil,nil]
  (-999..999).to_a.permutation(2).to_a.each do |pair|
    a = pair[0]
  	b = pair[1]
  	next unless Prime.prime?(a) && Prime.prime?(b)
      n = 0
      current_count = 0
      
      while Prime.prime?(n ** 2 + a*n + b)
        current_count += 1
        n += 1
      end

      if current_count > longest_count
        longest_count = current_count
        coefficients[0]= a
        coefficients[1] = b
      end
 
  end
   coefficients.reduce(:*)
end
p quadratic_primes