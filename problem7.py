import math
def is_prime(num):
  divisor = math.floor(math.sqrt(num))
  while (divisor >= 2):
    if (num % divisor == 0):
      return False
    divisor -= 1
  return True

def nth_prime(count, num = 2):
  while (count > 0):
    if (is_prime(num)):
      count -= 1
    num += 1
  return num - 1

print nth_prime(10001)
