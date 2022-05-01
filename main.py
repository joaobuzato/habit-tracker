import requests
import os
USERNAME = "joaobuzato"
TOKEN = os.environ.get("PIXELA_TOKEN")


PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": "ciclying",
    "name": "Ciclyng Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

cicle_params = {
    "date":"20220428",
    "quantity":"6.480"
}

response = requests.post(graph_endpoint+"/ciclying", json=cicle_params, headers=headers)
print(response.text)