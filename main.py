import requests as requests

USERNAME = "yukwok"
TOKEN = "234ghsf97shfkhsjfksdfsdfswrsfdf"

# USERNAME = "yukwokshanghai"
# TOKEN = "234ghsf97shfkhsjfksdfsdfswrsfdf"

PIXELA_URL = "https://pixe.la/v1"
CREATE_USER_ENDPOINT = "/users"
CREATE_GRAPH_ENDPOINT = f"/users/{USERNAME}/graphs"

params_create_user = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    }

# X-USER-TOKEN:thisissecret
headers = {
    "X-USER-TOKEN":TOKEN
}

params_create_graph = {
    "id": "graph1",
    "name": "Physical exercises - running",
    "unit": "km",
    "type": "float",
    "color": "sora",
}

# --- create user ---
# response = requests.post(url=f"{PIXELA_URL}{CREATE_USER_ENDPOINT}", json=params_create_user)

# --- create graph ----
response = requests.post(url=f"{PIXELA_URL}{CREATE_GRAPH_ENDPOINT}", json=params_create_graph, headers=headers)
print(response.text)
