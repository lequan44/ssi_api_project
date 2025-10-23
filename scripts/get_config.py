import json
import requests

#Declare file config
file_path = '../credentials/config.json'

#Open and read a JSON file
with open(file_path, "r") as file:
    config_data = json.load(file)

payload = {
    "consumerID": config_data["consumerID"],
    "consumerSecret": config_data["consumerSecret"]
}

headers = {
    "Content-Type": "application/json"
}

url = "https://fc-data.ssi.com.vn/api/v2/Market/AccessToken"
response = requests.post(url, json=payload, headers=headers)
if response.status_code == 200:
    access_token = response.json()['data'].get("accessToken")
else:
    print("Failed to get access token. Status Code:", response.status_code)
    print("Response Body:", response.text)
    exit()

print("Access token retrieved successfully")