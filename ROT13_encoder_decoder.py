alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

input_str = raw_input("Enter message that you would like to encrypt/decrypt using ROT13: ")
shift = 13
no_of_itr = len(input_str)
output_str = ""

for i in range(no_of_itr):
    current = input_str[i]
    location = alphabets.find(current)
    if location < 0:
        output_str += input_str[i]
    else:
        new_location = (location + shift)%26
        output_str += alphabets[new_location]

print "Here's the output: ", output_str