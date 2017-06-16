import math
import itertools

def is_prime(num):
  divisor = math.floor(math.sqrt(abs(num)))
  while (divisor >= 2):
    if (num % divisor == 0):
      return False
    divisor -= 1
  return True

def quadratic_primes():
  longest_count = 0
  coefficients = [0,0]
  nums = range(-999, 1000)
  permutations_list = list(itertools.permutations(nums,2))
  for pair in permutations_list:
    first_num = pair[0]
    second_num = pair[1]
    if (is_prime(first_num) == False and is_prime(second_num) == False):
      continue
    n = 0
    current_count = 0
    while (is_prime(n ** 2 + first_num * n + second_num)):
      current_count += 1
      n += 1

    if (current_count > longest_count):
      longest_count = current_count
      coefficients[0] = first_num
      coefficients[1] = second_num
  return coefficients[0] * coefficients[1]

print quadratic_primes()
