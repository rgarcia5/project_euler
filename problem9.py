import math
def pythagorean_triplet():
  a = 2
  while (a < 500):
    b = 2
    while (b < 500):
      c = math.sqrt(a ** 2 + b ** 2)
      if (a + b + c == 1000 and c % 1 == 0):
        return a*b*c
      b += 1
    a += 1


print pythagorean_triplet()
