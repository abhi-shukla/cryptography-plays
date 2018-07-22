import requests
import json
import operator

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

input_str = raw_input("Enter cipher to decode: ")
shift = int(raw_input("Enter your guess of shift: "))

n = len(input_str)
output_str = ""

app_id = 'your oxford dictionaries app id'
app_key = 'your oxford dictionaries app key'

language = 'en'
word_id = ''
base_url = 'https://od-api.oxforddictionaries.com:443/api/v1/search/'
query_divider = '?q='
prefix_param = '&prefix=true'
limit_param = '&limit=10'

# This function gets the meaning score of the potential plain text
def getScore(potential_plain_text):
	current_score = 0.0
	for temp in potential_plain_text:
		#Limiting the match of words with 4 alphabets or more makes it less likely for false positive
		if len(temp) > 3:
			url = base_url + language + query_divider + temp.lower() + prefix_param + limit_param
			r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})
			json_data = json.loads(r.text)
			if json_data['metadata']['total'] > 0 and json_data['results'][0]['score'] > 0:
				current_score += json_data['results'][0]['score']*json_data['metadata']['total']
	return current_score

class Result:
	def __init__(self, score, shift, plain_text):
		self.score = score
		self.shift = shift
		self.plain_text = plain_text
	def __getitem__(self, key):
		return self.result[key]

for k in range(n):
		c = input_str[k]
		location = alphabets.find(c)
		if location < 0:
		    output_str += input_str[k]
		else:
			new_location = (location - shift)%26
			output_str += alphabets[new_location]
data = output_str.split(" ", 20)
base_output_str = output_str
base_score = getScore(data[:20])


results = []

for i in range(26):
	output_str = ""

	for j in range(n):
		c = input_str[j]
		location = alphabets.find(c)
		if location < 0:
		    output_str += input_str[j]
		else:
			new_location = (location - i)%26
			output_str += alphabets[new_location]
	data = output_str.split(" ", 20)
	score = int(getScore(data[:20]))
	results.append(Result(score,i,output_str))

results.sort(key=operator.attrgetter('score'))
results.reverse()

print "Plain text from your guess: ", base_output_str, " - with shift: ", shift, " - the score is", base_score, "\n"

print "Below are the potential plain text sorted by the probability of being correct in descending order!"

for t in results:
	print "Potential plain text: ", t.plain_text, " - with shift: ", t.shift, " - the score is", t.score