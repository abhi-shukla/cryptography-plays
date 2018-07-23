import binascii

base_64_encoding_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=\\"

input_str = raw_input("Enter the base64 encoded string that you would like to decode: ")

error_count = 0;
output_str = input_str
depth = 0

def ValidateAndSplit(input_str):
	is_end = False
	n = len(input_str)
	if n < 1:
		is_end = True
		return input_str, is_end

	for i in range(n):
		c = input_str[i]
		location = base_64_encoding_characters.find(c)
		if location < 0 and c == " ":
			is_end = True
			break
		elif location < 0:
			data = input_str.split(c, 1)
			input_str = data[0]
			break

	return input_str, is_end
	

while error_count < 3:
	input_str, is_end = ValidateAndSplit(input_str.replace('\n',''))

	if is_end == True:
		break;
	try:
		temp = input_str.decode("base64")
		input_str = temp
		output_str = temp
		depth = depth + 1
		error_count = 0
		print input_str
	except binascii.Error as err:
		error_count = error_count + 1
		input_str = input_str + "="

print "Potential decoded string: ", output_str, "\nWith depth: ", depth