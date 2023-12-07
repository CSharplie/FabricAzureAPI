import requests, json
from settings import *

url = f"{root_url}?api-version={api_version}"
data = {
    "properties": {
        "administration" : {
            "members" : administrators
        }
    },
    "sku": {
        "name": sku,
        "tier": "Fabric"
    },
    "location": location
}


data_json = json.dumps(data)
result = requests.put(url=url, data=data_json, headers=headers)

print(f"Status: {result.status_code}")
print(f"Status: {result.content}")