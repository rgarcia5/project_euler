
ary = [0,1]
i = 1
sum = 0

while ary.last < 4_000_000
  ary << ary[i] + ary[i-1]
  if ary[i].even?
    sum += ary[i]
  end


  i += 1
end
