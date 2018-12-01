import requests
req = requests.get("https://api.github.com/events")
code = req.status_code
data = req.json()
print(req.json())

import json
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)