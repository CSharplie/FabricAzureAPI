import requests, json
from settings import *

url = f"{root_url}?api-version={api_version}"
result = requests.get(url=url, headers=headers)

print(f"Status: {result.status_code}")
print(f"Status: {result.content}")