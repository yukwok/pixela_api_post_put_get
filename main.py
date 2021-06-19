import requests as requests

url_create_user = "https://pixe.la/v1/users"

params_create_user = {
    "token": "234ghsf97shfkhsjfksdfsdfswrsfdf",
    "username": "yukwok",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    }

# --- create user ---
# response = requests.post(url=url_create_user, json=params_create_user)
print(response.json())
