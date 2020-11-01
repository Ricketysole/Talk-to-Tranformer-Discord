import requests, json

def generate_text(text):
	var = text
	endpoint = "https://api.inferkit.com/v1/models/standard/generate"
	data = json.dumps({
	  "prompt": {
	    "text": "{}".format(var)
	  },
	  "length": 500
	})
	headers = {"Authorization": "Bearer 0f058a4b-e73c-4d02-ac24-7838af159b84"}
	response = requests.post(endpoint, data=data, headers=headers).json()

	print(response)
	return (var + ' ' + response["data"]["text"])
