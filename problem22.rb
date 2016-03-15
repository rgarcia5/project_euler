
string_of_names = File.open("/home/rgarcia5/Desktop/project_euler/p022_names.txt")

list_of_names = string_of_names.read.split(",").sort
alphabet = ("A".."Z").to_a


result = 0
list_of_names.each do |name|
  
  name.each_char do |letter|
    next unless alphabet.include?(letter)
      result += (alphabet.index(letter) + 1) * (list_of_names.index(name) + 1)
    end

end

p result
