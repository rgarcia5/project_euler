  
def is_prime?(num)
  i = 3
  while i <= Math.sqrt(num)
    if num % i == 0
      return false
    end  
    i += 1
  end
  return true
end


def list_of_factors 
   num = 600851475143 
   i = 3
   factors = [] 
   prime_factors = []
     while num % i != 0 && i <= Math.sqrt(num) 
       i += 2 
         if num % i == 0 
           factors << i 
           num = num / i 
           factors << num    
         end 
      end 
   factors.sort.each do |num|
     if is_prime?(num)
       prime_factors << num 
     end
   end
  prime_factors.last
end 

list_of_factors



