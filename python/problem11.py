def set_array():
  result = []
  with open('problem11_numbers.txt', mode='r') as file:
    rows = file.read().split("\n")
  file.closed
  for row in rows:
    nums = row.split(" ")
    if (row != ""):
      result.append(list(map(lambda x: int(x), nums)))
  return result

DATA = set_array()

def left_diagonal():
  greatest_product = 0
  i = 0
  while (i < 16):
    j = 0
    while (j < 16):
      current_product = DATA[i][j] * DATA[i + 1][j + 1] * DATA[i+2][j+2] * DATA[i+3][j+3]
      if (current_product > greatest_product):
        greatest_product = current_product
      j += 1
    i += 1
  return greatest_product

def right_diagonal():
  greatest_product = 0
  i = 0
  while (i < 16):
    j = 19
    while (j > 3):
      current_product = DATA[i][j] * DATA[i+1][j-1] * DATA[i+2][j-2] * DATA[i+3][j-3]
      if (current_product > greatest_product):
        greatest_product = current_product
      j -=1
    i += 1
  return greatest_product

def vertical():
  greatest_product = 0
  i = 0
  while (i < 16):
    j = 0
    while (j < 16):
      current_product = DATA[j][i] * DATA[j+1][i] * DATA[j+2][i] * DATA[j+3][i]
      if (current_product > greatest_product):
        greatest_product = current_product
      j += 1
    i += 1
  return greatest_product

def horizontal():
  greatest_product = 0
  i = 0
  while (i < 16):
    j = 0
    while (j < 16):
      current_product = DATA[i][j] * DATA[i][j+1] * DATA[i][j+2] * DATA[i][j+3]
      if (current_product > greatest_product):
        greatest_product = current_product
      j += 1
    i += 1
  return greatest_product

def largest_product():
  return max([left_diagonal(), right_diagonal(), vertical(), horizontal()])

print largest_product()
