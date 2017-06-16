def power_digit_sum():
  num = 2 ** 1000
  num_string = str(num)
  result = 0
  for integer_string in num_string:
    integer = int(integer_string)
    result += integer
  return result

print power_digit_sum()
