def longest_collatz():
  i = 14
  longest_count = 0
  result = 0
  while (i < 1000000):
    current_count = 1
    current_num = i
    while (current_num != 1):
      if (current_num % 2 == 0):
        current_num /= 2
      else:
        current_num = current_num * 3 + 1
      current_count += 1
    if (current_count > longest_count):
      longest_count = current_count
      result = i
    i += 1
  return result

print longest_collatz()
