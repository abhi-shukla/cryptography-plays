input_str = raw_input("Enter the cipher text or plain text: ")
key = raw_input("Enter the key for encryption or decryption: ")
no_of_itr = len(input_str)
output_str = ""


for i in range(no_of_itr):
	current = input_str[i]
	current_key = key[i%len(key)]
	output_str += chr(ord(current) ^ ord(current_key))

print "Here's the output: ", output_str