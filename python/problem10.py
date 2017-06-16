import math
def sum_of_primes(num):
  nums = range(num+1)
  nums[1] = 0
  for i in range(4, num + 1, 2):
    nums[i] = 0
  for j in range(3, int(math.sqrt(num )) + 1, 2):
    if (nums[j]):
      for k in range(2 * nums[j], num + 1, nums[j]):
        nums[k] = 0
  return reduce((lambda x, y: x + y), nums)


print sum_of_primes(2000000)
