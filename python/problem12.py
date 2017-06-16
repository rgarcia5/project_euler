import math

def generate_triangular_num(n):
  return reduce((lambda x,y: x + y), range(1,n + 1))

def number_of_factors():
  i = 2
  while True:
    count = 0
    triangle_num = generate_triangular_num(i)
    j = 1
    while (j < math.sqrt(triangle_num)):
      if (triangle_num % j == 0):
        count += 2
      j +=1
    if (count >= 500):
      return triangle_num
    i += 1

print(number_of_factors())
