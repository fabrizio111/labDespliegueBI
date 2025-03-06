import requests

url = "http://127.0.0.1:8000/predict"
data = {
    "year": 2020,
    "km_driven": 50000,
    "u": 3.5,
    "g": 2.0,
    "class_GALAXY": 1,
    "class_STAR": 0
}

response = requests.post(url, json=data)
print(response.json())