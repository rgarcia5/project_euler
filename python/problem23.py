import math

def abundant_number(num):
  result = 1
  i = 2
  while (i <= math.sqrt(num)):
    if (num % i == 0):
      if(i ** 2 == num):
        result += num / i
      else:
        result += num / i + i
    i +=1
  if (result > num):
    return True
  else:
    return False

def sum_not_abundant():
  abundant_nums = []
  i = 1
  result = []
  while (i < 28124):
    if (abundant_number(i)):
      abundant_nums.append(i)
    i += 1
  for first_num in abundant_nums:
    for second_num in abundant_nums:
      pair_sum = first_num + second_num
      if (pair_sum > 28123):
        break
      else:
        result.append(pair_sum)
  numbers = range(1,28124)
  differences = list(set(numbers) - set(result))
  return reduce(lambda x,y: x + y, differences)

print sum_not_abundant()
