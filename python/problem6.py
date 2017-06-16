def square_of_sum(end_num, result = 0):
  if (end_num == 0):
    return result ** 2
  else:
    result += end_num
    return square_of_sum(end_num - 1, result)

def sum_of_squares(end_num,result = 0):
  if (end_num == 0):
    return result
  else:
    result += end_num ** 2
    return sum_of_squares(end_num - 1, result)

def difference(num):
  return square_of_sum(num) - sum_of_squares(num)

print difference(100)
