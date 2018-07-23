input_str = raw_input("Enter the string that you like to be base64 encoded:")
times = int(raw_input("How deep do you want it encoded:"))

output_str = input_str

for i in range(times):
	output_str = output_str.encode("base64")

print "Encoded string: ", output_str