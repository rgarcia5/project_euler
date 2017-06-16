def sum_nums():
  with open("problem13_numbers.txt", mode="r") as file:
    rows = file.readlines()
  file.closed
  result = reduce(lambda x,y: int(x) + int(y), rows)
  return str(result)[0:10] 
print sum_nums()
