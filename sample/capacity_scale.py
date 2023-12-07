import requests, json
from settings import *

url = f"{root_url}?api-version={api_version}"
data = {
    "sku": {
        "name": sku,
        "tier": "Fabric"
    }
}
data_json = json.dumps(data)
result = requests.patch(url=url, data=data_json, headers=headers)

print(f"Status: {result.status_code}")
print(f"Status: {result.content}")