import requests, json

def generate_text(text):
	endpoint = "https://api.inferkit.com/v1/models/standard/generate"
	#refer to https://inferkit.com/docs/generation-api to customize your data request
	data = json.dumps({
	  "prompt": {
	    "text": "{}".format(text)
	  },
	  "length": 500
	})
	headers = {"Authorization": "Bearer {your token here}"}
	response = requests.post(endpoint, data=data, headers=headers).json()

	return (text + ' ' + response["data"]["text"])
