import requests

url = "https://api.wassenger.com/v1/messages"

payload = "{\"phone\":\"+1234567890\",\"message\":\"Hello world! This is a test message\"}"
headers = {'token': '<api key>'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)