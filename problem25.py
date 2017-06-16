def fibonacci_sequence():
  count = 1
  first_num = 1
  second_num = 1
  while (len(str(first_num)) != 1000):
    result = first_num + second_num
    first_num = second_num
    second_num = result
    count += 1
  return count

print fibonacci_sequence()
