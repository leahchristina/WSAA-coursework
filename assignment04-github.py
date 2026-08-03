import os
import base64
import requests

# GitHub repository details
OWNER = "leahchristina"
REPO = "wsaa-private"
FILE_PATH = "api-test.txt"
BRANCH = "main"

# Read token from environment variable
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

# Check token exists
if GITHUB_TOKEN is None or GITHUB_TOKEN.strip() == "":
    raise ValueError("GITHUB_TOKEN is not set.")

# GitHub API URL
url = f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{FILE_PATH}"

# Request headers
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# Get the current file from GitHub
response = requests.get(url, headers=headers, params={"ref": BRANCH})

if response.status_code != 200:
    print("Could not read the file from GitHub.")
    print("Status code:", response.status_code)
    print("Response:", response.text)
    exit()

# Extract file data
file_data = response.json()

# The file content from GitHub is Base64 encoded
encoded_content = file_data["content"]
file_sha = file_data["sha"]

# Decode the file content so we can edit it as normal text
decoded_content = base64.b64decode(encoded_content).decode("utf-8")

# Replace Andrew with Leah
updated_content = decoded_content.replace("Andrew", "Leah")

# If nothing changed, do not commit
if updated_content == decoded_content:
    print("No changes needed. The file does not contain 'Andrew'.")
    exit()

# Encode the updated file content back to Base64
updated_encoded_content = base64.b64encode(
    updated_content.encode("utf-8")
).decode("utf-8")

# Data needed to update the file on GitHub
payload = {
    "message": 'Replace Andrew with Leah in api-test.txt',
    "content": updated_encoded_content,
    "sha": file_sha,
    "branch": BRANCH
}

# Send the updated file back to GitHub
update_response = requests.put(url, headers=headers, json=payload)

if update_response.status_code in [200, 201]:
    print