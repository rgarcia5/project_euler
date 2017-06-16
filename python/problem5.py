import math
def lowest_common_multiple(a,b):
  gcd , tmp = a, b
  while tmp != 0:
    gcd, tmp = tmp, gcd % tmp
  return a * (b/gcd)

nums = range(1,21)
while (len(nums) > 1):
  lcm = lowest_common_multiple(nums[0], nums[1])
  nums[0] = lcm
  del nums[1]

print nums[0]
