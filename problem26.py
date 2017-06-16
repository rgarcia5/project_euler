import math
def is_prime(num):
  divisor = math.floor(math.sqrt(num))
  while (divisor >= 2):
    if (num % divisor == 0):
      return False
    divisor -= 1
  return True

def length_of_repeats(num):
  digits = []
  remainder = 1 % num
  digits.append(remainder)
  while True:
    remainder *= 10
    digits.append(remainder % num)
    unique_values = list(set(digits))
    if (len(digits) - len(unique_values) > 0):
      break
  return len(digits) - 1

def reciprocal_cycles():
  greatest_repeats = 0
  i = 2
  while (i < 1000):
    if (is_prime(i)):
      current_repeat = length_of_repeats(i)
      if (greatest_repeats == 0 or current_repeat > length_of_repeats(greatest_repeats)):
        greatest_repeats = i
    i += 1
  return greatest_repeats

print reciprocal_cycles()
