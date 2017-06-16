def nums_to_words(n):
  conversion_dict = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand"
}
  result = ""
  for num,word in reversed(conversion_dict.items()):
    if (n == 0):
      return result
    elif (n <= 10 and n/num > 0):
      return result + word
    elif (n < 100 and n/num > 0):
      if(n%num == 0):
        return result + word
      return result + word + nums_to_words(n%num)
    elif (n/num > 0):
      if (n%num == 0):
        return result + nums_to_words(n/num) + word
      return result + nums_to_words(n/num) + word + "and" + nums_to_words(n%num)

def letter_count(num):
  i = 1
  count = 0
  while (i <=num):
    word = nums_to_words(i)
    count += len(word)
    i += 1
  return count

print letter_count(1000)
