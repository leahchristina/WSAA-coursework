import requests
import os

token = os.getenv("TOKEN")

headers = {
    "Authorization": f"token {token}"
}

url = "https://api.github.com/repos/leahchristina/wsaa-private/contents/api-test.txt"

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())