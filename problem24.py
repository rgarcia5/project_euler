import itertools
def millionth_permutation():
  nums = range(0,10)
  permutation_list = list(itertools.permutations(nums))
  return permutation_list[999999]

print "".join(str(i) for i in millionth_permutation()) 
