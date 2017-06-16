import math
def sum_divisors(num):
  i = 2
  result = 1
  while (i <= math.sqrt(num)):
    if (num % i == 0):
      result +=  (num / i) + i
    i += 1
  return result

def prime_number(num):
  divisor = math.floor(math.sqrt(num))
  while (divisor >= 2):
    if (num % divisor == 0):
      return False
    divisor -= 1
  return True

def sum_amicable_nums():
  result = 0
  list_of_sums = {}
  for num in range(1, 10001):
    if (prime_number(num)):
      continue
    if sum_divisors(num) in list_of_sums and list_of_sums[sum_divisors(num)] == num:
      result += num + sum_divisors(num)
    else:
      list_of_sums[num] = sum_divisors(num)
  return result

print sum_amicable_nums()
