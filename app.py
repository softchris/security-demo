# create python app that calls a random qeb api with an API token

import requests

# API URL
url = "https://api.quotable.io/random"

# API Token
api_token = "1234"
azure_search_admin_key = "1234"

# make a request to the API
response = requests.get(url, headers={"Authorization": f"Bearer {api_token}"})

# print the response
print(response.json())
