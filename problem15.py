def factorial(num):
  if (num == 0):
    return 1
  return reduce(lambda x,y: x * y, range(1,num + 1))

def number_of_paths(grid_size):
  return factorial(grid_size * 2)/ (factorial(grid_size) ** 2)

print number_of_paths(20)
