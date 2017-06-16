def is_palindrome(num):
  string = str(num)
  i = 0
  while (i < len(string)):
    if (string[i] != string[len(string) - i - 1]):
      return False
    i += 1
  return True

def largest_product():
  i = 999
  result = 0
  while (i > 0):
    j = i
    while (j > 0):
      if (is_palindrome(i * j) and i *j > result):
        result = i * j
      j -= 1
    i -= 1
  return result

print largest_product()
