
def sum_of_squares
  (1..100).inject{ |sum,n| sum + n**2}
end

def sum
  (1..100).inject{ |sum,n| sum + n}
end
def
 square_of_sums
  sum ** 2
end

def difference
  square_of_sums - sum_of_squares
end

