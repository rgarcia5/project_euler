def sum_of_fifth_powers():
  upper_limit = 5 * (9 ** 5)
  i = 2
  result = 0
  while (i < upper_limit):
    new_num = i
    num_string = str(i)
    string_idx = 0
    while (string_idx < len(num_string)):
      digit = int(num_string[string_idx])
      new_num -= digit ** 5
      string_idx += 1
    if (new_num == 0):
      result += i
    i += 1
  return result

print sum_of_fifth_powers()
