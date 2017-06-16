
def sum_digits(n):
  num = reduce(lambda x,y: x*y, range(1,n + 1))
  numstring = str(num)
  result = 0
  for i in numstring:
    result += int(i)
  return result

print sum_digits(100)
