import requests
import json  

message = {"message": "Connected to the client!"}
url = "http://127.0.0.1:8888/api/messages"

headers = {"Content-Type": "application/json"}  

response = requests.post(url, json=message, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(data["status"])
else:
    print("Failed to communicate with the server.")
