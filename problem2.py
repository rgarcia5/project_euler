def fibonacci_numbers():
  first_num = 0
  second_num = 1
  result = 0
  while (second_num < 4000000):
    fibonacci_num = first_num + second_num
    if (fibonacci_num % 2 == 0):
      result += fibonacci_num
    first_num = second_num
    second_num = fibonacci_num
  return result

print fibonacci_numbers()
