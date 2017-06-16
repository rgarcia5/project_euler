import math
def is_prime(num):
  divisor = math.floor(math.sqrt(num))
  while (divisor >= 2):
    if (num % divisor == 0):
      return False
    divisor -= 1
  return True

def largest_prime_factor(num):
  divisor = math.floor(math.sqrt(num))
  while (divisor > 0):
    if (num % divisor == 0 and is_prime(divisor)):
      return divisor
    divisor -= 1

print largest_prime_factor(600851475143)
