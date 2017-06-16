def list_of_nums():
  with open("problem18_numbers.txt", mode="r") as file:
    nums = file.read().split("\n")
  file.closed
  result = []
  for row in nums:
    num_strings = row.split(" ")
    if (num_strings != [""]):
      result.append(map(lambda x: int(x), row.split(" ")))
  return result

def max_path_sum():
  nums = list_of_nums()
  i = 13
  while (i >= 0):
    j = 0
    while (j < len(nums[i])):
      nums[i][j] +=  max([nums[i + 1][j], nums[i+1][j+1]])
      j += 1
    i -= 1
  return nums[0][0]

print max_path_sum()
