import json

import requests
URL = "https://reqres.in/api/users?page=2"


#resp = response.content

#resp = json.loads(resp)

#print(json.dumps(resp.get('data')[0],indent=4))

#print(response.json())

response = requests.get(URL)
resp_dict = response.json()

print(resp_dict.get("page"))