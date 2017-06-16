def sprial_diagonals(length):
  result = 1
  i = 3
  while (i <= length):
    if (i % 2 > 0):
      result += i ** 2
      j = 1
      while (j < 4):
        result += (i ** 2 - (i - 1) * j)
        j += 1
    i += 1
  return result

print (sprial_diagonals(1001))
