def distinct_powers():
  bases = range(2,101)
  exponents = range(2,101)
  result = []
  for base in bases:
    for exponent in exponents:
      value = base ** exponent
      if (value in result):
        continue
      else:
        result.append(base ** exponent)
  return len(result)
print(distinct_powers())
