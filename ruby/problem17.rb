def single_digit
  ary = ["one","two","three","four","five","six","seven","eight","nine"]
end

def teens
  ary = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
end

def tens
  ary = ["ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
end

def hundreds
  ary = "hundred"
end

def thousands
  ary = "thousand"
end


def convert_to_words(num)
  digits =  num.to_s.split("").map{ |num| num.to_i}
  word = ""
  while digits.length > 0
    if digits.length == 4
      word += single_digit[digits.first - 1] + thousands
      break
    elsif digits.length == 3
      if digits.join("").to_i % 100 == 0
      	word += single_digit[digits.first - 1] + hundreds
      	break
      else
        word += single_digit[digits.first - 1] + hundreds + "and"
      end
    elsif digits.length == 2
      if digits.first == 0
      	digits.delete_at(0)
      	next
      elsif digits.first == 1 
      	if digits.last == 0
          word += tens[digits.first - 1]
        else      		
      	  word += teens[digits.last - 1] 

      	end
      	break
         
      elsif digits.join("").to_i % 10 == 0
      	word += tens[digits.first - 1]
      	break
      else
      	word += tens[digits.first - 1]
      end

    elsif digits.length == 1 
      word += single_digit[digits.first - 1]

    end
   
    digits.delete_at(0)

  end

  word

end


def letter_count
  
  count = 0
  1.upto(1000) do |num| 
    
    convert_to_words(num).chars.each do |digit|
      count += 1
    end
   
   end
  count
end

p letter_count
