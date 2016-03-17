def distinct_powers
  bases = (2..100).to_a
  exponent = (2..100).to_a
  terms = []
  bases.each do |base|
    exponent.each do |exp|
      terms << base ** exp    
    end
  end

  terms.uniq.length

end

p distinct_powers