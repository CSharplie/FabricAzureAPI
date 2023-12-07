import requests, json
from settings import *

url = f"{root_url}/resume?api-version={api_version}"
result = requests.post(url=url, headers=headers)

print(f"Status: {result.status_code}")
print(f"Status: {result.content}")