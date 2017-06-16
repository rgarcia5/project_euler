import string
def get_names():
  with open("p022_names.txt", mode = "r") as file:
    result = file.read().split(",")
  file.closed
  return sorted(map(lambda x: x.replace("\"", ""), result))


alphabet = list(string.ascii_uppercase)

def names_scores():
  list_of_names = get_names()
  score = 0
  for name in list_of_names:
    for letter in name:
      score += (alphabet.index(letter) + 1) * (list_of_names.index(name) + 1)
  return score

print names_scores()
